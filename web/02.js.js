let people = ["Bromald Bump", "Billary Dimpton", "Pal Dore"];

function cycle(){
  let peoplesVote = Math.floor(Math.random() * 10 % 3);
  document.getElementById('singature').innerHTML = people[peoplesVote];
}

setInterval(cycle, 1000)
