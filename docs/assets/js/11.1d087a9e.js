(window.webpackJsonp=window.webpackJsonp||[]).push([[11],{369:function(t,e,n){"use strict";var i=n(44),l=n(6),r=n(3),s=n(198),o=n(197),u=n(10),a=n(33),c=n(119),d=n(199),p=n(92),h=n(16),v=n(63),g=n(202),f=n(200),x=n(94),b=n(196),m=n(2),_=b.UNSUPPORTED_Y,C=Math.min,w=[].push,y=r(/./.exec),I=r(w),B=r("".slice);s("split",(function(t,e,n){var r;return r="c"=="abbc".split(/(b)*/)[1]||4!="test".split(/(?:)/,-1).length||2!="ab".split(/(?:ab)*/).length||4!=".".split(/(.?)(.?)/).length||".".split(/()()/).length>1||"".split(/.?/).length?function(t,n){var r=h(a(this)),s=void 0===n?4294967295:n>>>0;if(0===s)return[];if(void 0===t)return[r];if(!o(t))return l(e,r,t,s);for(var u,c,d,p=[],v=(t.ignoreCase?"i":"")+(t.multiline?"m":"")+(t.unicode?"u":"")+(t.sticky?"y":""),f=0,b=new RegExp(t.source,v+"g");(u=l(x,b,r))&&!((c=b.lastIndex)>f&&(I(p,B(r,f,u.index)),u.length>1&&u.index<r.length&&i(w,p,g(u,1)),d=u[0].length,f=c,p.length>=s));)b.lastIndex===u.index&&b.lastIndex++;return f===r.length?!d&&y(b,"")||I(p,""):I(p,B(r,f)),p.length>s?g(p,0,s):p}:"0".split(void 0,0).length?function(t,n){return void 0===t&&0===n?[]:l(e,this,t,n)}:e,[function(e,n){var i=a(this),s=null==e?void 0:v(e,t);return s?l(s,e,i,n):l(r,h(i),e,n)},function(t,i){var l=u(this),s=h(t),o=n(r,l,s,i,r!==e);if(o.done)return o.value;var a=c(l,RegExp),v=l.unicode,g=(l.ignoreCase?"i":"")+(l.multiline?"m":"")+(l.unicode?"u":"")+(_?"g":"y"),x=new a(_?"^(?:"+l.source+")":l,g),b=void 0===i?4294967295:i>>>0;if(0===b)return[];if(0===s.length)return null===f(x,s)?[s]:[];for(var m=0,w=0,y=[];w<s.length;){x.lastIndex=_?0:w;var E,F=f(x,_?B(s,w):s);if(null===F||(E=C(p(x.lastIndex+(_?w:0)),s.length))===m)w=d(s,w,v);else{if(I(y,B(s,m,w)),y.length===b)return y;for(var T=1;T<=F.length-1;T++)if(I(y,F[T]),y.length===b)return y;w=m=E}}return I(y,B(s,m)),y}]}),!!m((function(){var t=/(?:)/,e=t.exec;t.exec=function(){return e.apply(this,arguments)};var n="ab".split(t);return 2!==n.length||"a"!==n[0]||"b"!==n[1]})),_)},398:function(t,e,n){},462:function(t,e,n){"use strict";n(398)},479:function(t,e,n){"use strict";n.r(e);n(32),n(369);var i={props:["gridTemplateColumns","columnGap"],computed:{addStyle:function(){return{"--col":this.gridTemplateColumns,"--col-gap":this.columnGap}},textForBox:function(){return this.gridTemplateColumns.split(" ")}}},l=(n(462),n(62)),r=Object(l.a)(i,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"layout",style:t.addStyle},[n("div",{staticClass:"box box1"},[n("p",[t._v(t._s(t.textForBox[0]))])]),t._v(" "),n("div",{staticClass:"box box2"},[n("p",[t._v(t._s(t.textForBox[1]))])]),t._v(" "),n("div",{staticClass:"box box3"},[n("p",[t._v(t._s(t.textForBox[2]))])])])}),[],!1,null,"144755c4",null);e.default=r.exports}}]);