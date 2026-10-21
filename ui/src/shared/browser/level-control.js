export function createLevelControl(input, label) {
  const group = document.createElement('span');
  group.className = 'db-level-control';
  input.type = 'range'; input.step = '1'; input.setAttribute('aria-label', label);
  input.before(group);
  const output = document.createElement('output'); output.htmlFor = input.id;
  const buttons = [-10,-1,1,10].map(step => {
    const button = document.createElement('button'); button.type = 'button';
    button.textContent = step===-10?'◀◀':step===-1?'◀':step===1?'▶':'▶▶';
    button.title = label+'を'+Math.abs(step)+(step<0?'下げる':'上げる');
    button.setAttribute('aria-label',button.title);
    button.addEventListener('click',event=>{event.preventDefault();input.stepUp(step);input.dispatchEvent(new Event('input',{bubbles:true}));});
    return {button,step};
  });
  group.append(buttons[0].button,buttons[1].button,input,buttons[2].button,buttons[3].button,output);
  function sync(maximum) {
    if(maximum!=null)input.max=String(maximum);
    output.value=input.value;
    for(const {button,step} of buttons)button.disabled=input.disabled||(step<0?Number(input.value)<=Number(input.min):Number(input.value)>=Number(input.max));
  }
  input.addEventListener('input',()=>sync());sync();
  return {sync,output};
}
