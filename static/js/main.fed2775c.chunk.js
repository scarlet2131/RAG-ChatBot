(this["webpackJsonpmy-chatbot"]=this["webpackJsonpmy-chatbot"]||[]).push([[0],{17:function(e,t,a){},18:function(e,t,a){},23:function(e,t,a){"use strict";a.r(t);var n=a(2),r=a.n(n),s=a(7),c=a.n(s),o=(a(17),a(18),a(25));var l=e=>{let{sender:t,text:a}=e;return r.a.createElement("div",{className:"message ".concat(t)},a)};var m=e=>{let{messages:t}=e;return r.a.createElement("div",{className:"message-list"},t.map((e,t)=>r.a.createElement(l,{key:t,sender:e.sender,text:e.text})))};var u=e=>{let{onSendMessage:t}=e;const[a,s]=Object(n.useState)("");return r.a.createElement("form",{className:"message-input",onSubmit:e=>{e.preventDefault(),a.trim()&&(t(a),s(""))}},r.a.createElement("input",{type:"text",value:a,onChange:e=>s(e.target.value),placeholder:"Type your message here..."}),r.a.createElement("button",{type:"submit"},"Send"))};var d=()=>{const[e,t]=Object(n.useState)([]);return r.a.createElement("div",{className:"chat-window"},r.a.createElement("div",{className:"chat-header"},"Chatbot"),r.a.createElement(m,{messages:e}),r.a.createElement(u,{onSendMessage:async a=>{const n={sender:"user",text:a};t([...e,n]);try{const r=await o.a.post("http://localhost:8000/chat",{que:a},{headers:{"Content-Type":"application/json"}});let s;s=r.data.response?{sender:"bot",text:r.data.response}:r.data.error?{sender:"bot",text:r.data.error}:{sender:"bot",text:"An unknown error occurred."},t([...e,n,s])}catch(r){console.error("Error sending message:",r)}}}))};var i=function(){return r.a.createElement("div",{className:"App"},r.a.createElement(d,null))};var p=e=>{e&&e instanceof Function&&a.e(3).then(a.bind(null,26)).then(t=>{let{getCLS:a,getFID:n,getFCP:r,getLCP:s,getTTFB:c}=t;a(e),n(e),r(e),s(e),c(e)})};c.a.createRoot(document.getElementById("root")).render(r.a.createElement(r.a.StrictMode,null,r.a.createElement(i,null))),p()},8:function(e,t,a){e.exports=a(23)}},[[8,1,2]]]);
//# sourceMappingURL=main.fed2775c.chunk.js.map