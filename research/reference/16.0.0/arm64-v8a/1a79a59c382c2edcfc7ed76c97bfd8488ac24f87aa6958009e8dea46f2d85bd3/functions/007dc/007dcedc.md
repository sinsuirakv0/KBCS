# 007dcedc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "007dcedc",
  "name": "FUN_007dcedc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "927b43fe6e528fb0f142b6b0df7c32d49246d04398eb0868fb7bce39565baddd",
  "source_text_sha256": "927b43fe6e528fb0f142b6b0df7c32d49246d04398eb0868fb7bce39565baddd"
}
~~~

## 呼び出し元

- [007cceac](../007cc/007cceac.md)
- [0089e838](../0089e/0089e838.md)
- [00bf85ec](../00bf8/00bf85ec.md)

## 呼び出し先

- [00c57b80](../00c57/00c57b80.md)

## 疑似コード / UTF-8 389 bytes

~~~c

void FUN_007dcedc(undefined8 param_1,byte *param_2)

{
  ulong uVar1;
  byte *pbVar2;
  
  uVar1 = *(ulong *)(param_2 + 8);
  pbVar2 = *(byte **)(param_2 + 0x10);
  if ((*param_2 & 1) == 0) {
    pbVar2 = param_2 + 1;
    uVar1 = (ulong)(*param_2 >> 1);
  }
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
            (param_1,pbVar2,uVar1);
  return;
}

~~~
