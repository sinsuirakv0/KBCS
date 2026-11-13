# 005cefbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "005cefbc",
  "name": "FUN_005cefbc",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f56aa53d419c36d27df3396e09301b5a8cb414b4dc7603570eeda33e181888a1",
  "source_text_sha256": "f56aa53d419c36d27df3396e09301b5a8cb414b4dc7603570eeda33e181888a1"
}
~~~

## 呼び出し元

- [005ce640](../005ce/005ce640.md)

## 呼び出し先

- [00c58350](../00c58/00c58350.md)
- [00c5a870](../00c5a/00c5a870.md)

## 疑似コード / UTF-8 584 bytes

~~~c

void FUN_005cefbc(long param_1)

{
  undefined8 uVar1;
  
  _ZNSt6__ndk16localeC2Ev();
  uVar1 = _ZNKSt6__ndk16locale9use_facetERNS0_2idE(param_1,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9ad00);
  *(undefined8 *)(param_1 + 8) = uVar1;
  uVar1 = _ZNKSt6__ndk16locale9use_facetERNS0_2idE(param_1,PTR__ZNSt6__ndk17collateIcE2idE_00c9b448)
  ;
  *(undefined8 *)(param_1 + 0x10) = uVar1;
  *(undefined8 *)(param_1 + 0x20) = 0;
  *(undefined8 *)(param_1 + 0x18) = 0;
  *(undefined8 *)(param_1 + 0x30) = 0;
  *(undefined8 *)(param_1 + 0x28) = 0;
  *(undefined8 *)(param_1 + 0x38) = 0;
  return;
}

~~~
