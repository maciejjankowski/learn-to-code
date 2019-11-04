(function(delay) {
  function exportTableToCSV($table, filename) {
    var $rows = $table.find('tr:has(td,th)'),
      tmpColDelim = String.fromCharCode(11),
      tmpRowDelim = String.fromCharCode(0), 
      colDelim = '"\t"',
      rowDelim = '"\r\n"',

      csv =
        '"' +
        $rows
          .map(function(i, row) {
            var $row = $(row),
              $cols = $row.find('td,th');

            return $cols
              .map(function(j, col) {
                var $col = $(col),
                  text = $col.text();

                return text.replace(/"/g, '""'); 
              })
              .get()
              .join(tmpColDelim);
          })
          .get()
          .join(tmpRowDelim)
          .split(tmpRowDelim)
          .join(rowDelim)
          .split(tmpColDelim)
          .join(colDelim) +
        '"';

    // Data URI
    var bom = decodeURIComponent('%EF%BB%BF'); 
    var byteArray = [];
    csv = bom + csv;

    csvA = new Uint16Array(
      csv.split('').map(function(k, v) {
        return k.charCodeAt(0);
      })
    );

    var blob = new Blob([csvA], { type: 'text/csv;charset=UTF-16LE;' });
    var blobUrl = URL.createObjectURL(blob);

    return blobUrl;
  }

  function download(filename, text) {
    var pom = document.createElement('a');
    pom.setAttribute('href', text);
    pom.setAttribute('download', filename);

    if (document.createEvent) {
      var event = document.createEvent('MouseEvents');
      event.initEvent('click', true, true);
      pom.dispatchEvent(event);
    } else {
      pom.click();
    }
  }

  function downloadAll(out) {
    download(
      'raport.csv',
      exportTableToCSV(
        $(out.document.getElementsByTagName('table')[0]),
        'raport.tsv'
      )
    );
    out.close();
  }

  var xfields = [
    'MainContent_lblNip',
    'MainContent_lblName',
    'MainContent_lblEmail',
    'MainContent_lblWebstite',
    'MainContent_lblCorrespondenceAddress',
    'MainContent_lblDateOfCommencementOfBusiness'
  ];

  function extractCompanyData(data) {
    var i = 0;
    var obj = [];
    xfields.forEach(function(el) {
      var value = data.match(el + '.+>(.+?)<'); 
      value = value ? value[1] : '';
      el = el.replace('MainContent_lbl', '');
      obj[i++] = decodeEntities(value);
    });
    let pkd = data.match(/PKD2007'>(.+?)</g);
    pkdOpis = data.match(/PKD.+?<b>(.+?)</);
    pkdOpis = pkdOpis ? pkdOpis[1] : '';
    Array.prototype.forEach.call(pkd || [], function(el, index) {
      pkd[index] = el.replace("PKD2007'>", '').replace('<', '');
    });
    obj[i++] = pkdOpis;
    obj[i++] = (pkd || '') && pkd.join(' ');
    return obj;
  }

  async function getContents(delay, href, i, a) {
    console.log(arguments);
    const p1 = new Promise(resolve => {
      setTimeout(() => {
        resolve(fetch(href).then(r => r.text()));
        console.log('pobieranie', href);
      }, Math.ceil(Math.random() * a.length * delay));
    });

    return p1;
  }

  var decodeEntities = (function() {
    var element = document.createElement('div');
    function decodeHTMLEntities(str) {
      if (str && typeof str === 'string') {
        let r1 = new RegExp("<sc.ipt[^>]*>([\S\s]*?)<\/sc.ipt>", "gim")
        let r2 = new RegExp(`<\/?\w(?:[^"'>]|"[^"]*"|'[^']*')*>`,"gim")
        str = str.replace(r1, '');
        str = str.replace(r2, '');
        element.innerHTML = str;
        str = element.textContent;
        element.textContent = '';
      }
      return str;
    }
    return decodeHTMLEntities;
  })();

  function toTRText(o) {
    return (
      '<tr><td>' + Array.prototype.join.call(o, '</td><td>') + '</td></tr>'
    );
  }
  function writeResultRow(text, out) {
    out.document.write(text);
  }

  (function _getData() {
    var obrazki = document.querySelectorAll('img[src="../Images/View.png"]'); // łapiemy wszystkie linki z obrazkiem

    const allRecordsData = Array.from(obrazki)
      .map(obrazek => obrazek.parentElement.href)
      .map(getContents.bind(null, delay));

    Promise.all(allRecordsData).then(results => {
      var out = window.open('', out, 'width=400,height=400,top=900,left=700');
      out.document.write('<html><head></head><body><table border="1">');

      const resultsText = results
        .map(extractCompanyData)
        .map(toTRText)
        .join('');
      writeResultRow(resultsText, out);

      downloadAll(out);
    });
  })();
})(localStorage.delay || 600);
