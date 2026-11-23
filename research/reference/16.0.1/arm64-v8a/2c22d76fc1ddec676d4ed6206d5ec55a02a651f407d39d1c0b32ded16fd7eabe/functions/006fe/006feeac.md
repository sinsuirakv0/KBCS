# 006feeac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/review-0060.md#review-7c72c8a0900d2bd5062f11f45a37ac5e)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/review-0021.md#review-7c72c8a0900d2bd5062f11f45a37ac5e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006feeac",
  "name": "FUN_006feeac",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7b425710763e212af9fa75101b9204ac0ac4c51ac9912187fcf730aaecfc92ba",
  "source_text_sha256": "7b425710763e212af9fa75101b9204ac0ac4c51ac9912187fcf730aaecfc92ba"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [006b7130](../006b7/006b7130.md)
- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 709 bytes

~~~c

void FUN_006feeac(undefined8 param_1,char *param_2)

{
  char cVar1;
  long lVar2;
  
  cVar1 = *param_2;
  lVar2 = FUN_008514f8();
  if (cVar1 == '\0') {
    FUN_008514f8();
    FUN_006b7130(lVar2 + 0x42ef60,0,0,1);
  }
  else {
                    /* try { // try from 006feed4 to 007fef2f has its CatchHandler @ 00704bfc */
    if (0.0 < *(double *)(BYTE_ARRAY_0042ef4d + lVar2 + 0x23)) {
      lVar2 = FUN_008514f8();
      FUN_008514f8();
      FUN_006b7130(lVar2 + 0x42ef60,0,1,1);
    }
    lVar2 = FUN_008514f8();
    if (*(double *)((long)&DWORD_0042ef78 + lVar2) <= 0.0) {
      return;
    }
  }
  lVar2 = FUN_008514f8();
  FUN_008514f8();
  FUN_006b7130(lVar2 + 0x42ef60,1,cVar1,1);
  return;
}

~~~
