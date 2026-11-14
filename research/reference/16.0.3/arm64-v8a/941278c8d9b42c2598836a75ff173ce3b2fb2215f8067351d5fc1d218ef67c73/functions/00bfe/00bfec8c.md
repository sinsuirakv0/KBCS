# 00bfec8c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfec8c",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPcl",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0e46543673319600f24eaf07630290dc6a496673e065d95d3c703076c96601e3",
  "source_text_sha256": "0e46543673319600f24eaf07630290dc6a496673e065d95d3c703076c96601e3"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c59310](../00c59/00c59310.md)
- [00c59320](../00c59/00c59320.md)
- [00c59330](../00c59/00c59330.md)
- [00c5f430](../00c5f/00c5f430.md)

## 疑似コード / UTF-8 644 bytes

~~~c

void _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPcl
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  undefined4 uVar1;
  long *plVar2;
  undefined1 auStack_38 [8];
  
  _ZNKSt6__ndk18ios_base6getlocEv(auStack_38,(long)param_1 + *(long *)(*param_1 + -0x18));
  plVar2 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                             (auStack_38,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9bcd0);
  uVar1 = (**(code **)(*plVar2 + 0x38))(plVar2,10);
  _ZNSt6__ndk16localeD1Ev(auStack_38);
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPclc(param_1,param_2,param_3,uVar1);
  return;
}

~~~
