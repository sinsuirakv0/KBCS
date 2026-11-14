# 00bffeac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bffeac",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEy",
  "size": 300,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a23b8b2b10ca16054b839cafe070096e7386cea7076278fd31202a5f13eb4fea",
  "source_text_sha256": "a23b8b2b10ca16054b839cafe070096e7386cea7076278fd31202a5f13eb4fea"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c59300](../00c59/00c59300.md)
- [00c59310](../00c59/00c59310.md)
- [00c59320](../00c59/00c59320.md)
- [00c59330](../00c59/00c59330.md)
- [00c59340](../00c59/00c59340.md)
- [00c59350](../00c59/00c59350.md)

## 疑似コード / UTF-8 1629 bytes

~~~c

long * _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEy(long *param_1,undefined8 param_2)

{
  uint uVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  undefined8 uVar5;
  char local_58 [16];
  undefined1 auStack_48 [8];
  
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_(local_58,param_1);
  if (local_58[0] != '\0') {
    _ZNKSt6__ndk18ios_base6getlocEv(auStack_48,(long)param_1 + *(long *)(*param_1 + -0x18));
    plVar2 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                               (auStack_48,
                                PTR__ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9c8d8
                               );
    _ZNSt6__ndk16localeD1Ev(auStack_48);
    lVar4 = (long)param_1 + *(long *)(*param_1 + -0x18);
    uVar1 = *(uint *)(lVar4 + 0x90);
    uVar5 = *(undefined8 *)(lVar4 + 0x28);
    if (uVar1 == 0xffffffff) {
      _ZNKSt6__ndk18ios_base6getlocEv(auStack_48,lVar4);
      plVar3 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                                 (auStack_48,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9bcd0);
      uVar1 = (**(code **)(*plVar3 + 0x38))(plVar3,0x20);
      _ZNSt6__ndk16localeD1Ev(auStack_48);
      uVar1 = uVar1 & 0xff;
      *(uint *)(lVar4 + 0x90) = uVar1;
    }
    lVar4 = (**(code **)(*plVar2 + 0x38))(plVar2,uVar5,lVar4,uVar1,param_2);
    if (lVar4 == 0) {
      lVar4 = (long)param_1 + *(long *)(*param_1 + -0x18);
      _ZNSt6__ndk18ios_base5clearEj(lVar4,*(uint *)(lVar4 + 0x20) | 5);
    }
  }
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryD2Ev(local_58);
  return param_1;
}

~~~
