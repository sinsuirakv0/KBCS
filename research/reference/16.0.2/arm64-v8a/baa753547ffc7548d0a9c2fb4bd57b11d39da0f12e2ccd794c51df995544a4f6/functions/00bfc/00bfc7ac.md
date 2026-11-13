# 00bfc7ac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bfc7ac",
  "name": "FUN_00bfc7ac",
  "size": 256,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d72e4a7d80a0f004a9cb97ce209d4ac37a963160d1d82decd0cda36a8d3be210",
  "source_text_sha256": "d72e4a7d80a0f004a9cb97ce209d4ac37a963160d1d82decd0cda36a8d3be210"
}
~~~

## 呼び出し元

- [00bfc7a4](../00bfc/00bfc7a4.md)

## 呼び出し先

- [00c58340](../00c58/00c58340.md)
- [00c58350](../00c58/00c58350.md)
- [00c58360](../00c58/00c58360.md)
- [00c58370](../00c58/00c58370.md)
- [00c59ea0](../00c59/00c59ea0.md)

## 疑似コード / UTF-8 1282 bytes

~~~c

long * FUN_00bfc7ac(long *param_1,undefined2 *param_2)

{
  long lVar1;
  long *plVar2;
  undefined2 uVar3;
  undefined1 auStack_38 [8];
  long local_30;
  char local_28 [4];
  uint local_24;
  
  local_24 = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_28,param_1,0);
  if (local_28[0] == '\0') {
    return param_1;
  }
  _ZNKSt6__ndk18ios_base6getlocEv(auStack_38,(long)param_1 + *(long *)(*param_1 + -0x18));
  plVar2 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                             (auStack_38,
                              PTR__ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9bbe0
                             );
  lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
  (**(code **)(*plVar2 + 0x20))(plVar2,*(undefined8 *)(lVar1 + 0x28),0,lVar1,&local_24,&local_30);
  _ZNSt6__ndk16localeD1Ev(auStack_38);
  if (local_30 < -0x8000) {
    uVar3 = 0x8000;
  }
  else {
    if (local_30 < 0x8000) {
      *param_2 = (short)local_30;
      goto LAB_00bfc878;
    }
    uVar3 = 0x7fff;
  }
  local_24 = local_24 | 4;
  *param_2 = uVar3;
LAB_00bfc878:
  lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
  _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | local_24);
  return param_1;
}

~~~
