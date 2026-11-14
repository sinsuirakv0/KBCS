# 00bfdbcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfdbcc",
  "name": "FUN_00bfdbcc",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6b2b8849f57902c80b86940599f8893f405609c5738731cfe9a96ad9bd9eefb6",
  "source_text_sha256": "6b2b8849f57902c80b86940599f8893f405609c5738731cfe9a96ad9bd9eefb6"
}
~~~

## 呼び出し元

- [00bfdbc4](../00bfd/00bfdbc4.md)

## 呼び出し先

- [00c59310](../00c59/00c59310.md)
- [00c59320](../00c59/00c59320.md)
- [00c59330](../00c59/00c59330.md)
- [00c59340](../00c59/00c59340.md)
- [00c5ae70](../00c5a/00c5ae70.md)

## 疑似コード / UTF-8 1002 bytes

~~~c

long * FUN_00bfdbcc(long *param_1,undefined8 param_2)

{
  long lVar1;
  long *plVar2;
  undefined1 auStack_30 [8];
  char local_28 [4];
  uint local_24;
  
  local_24 = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_28,param_1,0);
  if (local_28[0] != '\0') {
    _ZNKSt6__ndk18ios_base6getlocEv(auStack_30,(long)param_1 + *(long *)(*param_1 + -0x18));
    plVar2 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                               (auStack_30,
                                PTR__ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9cbb0
                               );
    lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
    (**(code **)(*plVar2 + 0x38))(plVar2,*(undefined8 *)(lVar1 + 0x28),0,lVar1,&local_24,param_2);
    _ZNSt6__ndk16localeD1Ev(auStack_30);
    lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
    _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | local_24);
  }
  return param_1;
}

~~~
