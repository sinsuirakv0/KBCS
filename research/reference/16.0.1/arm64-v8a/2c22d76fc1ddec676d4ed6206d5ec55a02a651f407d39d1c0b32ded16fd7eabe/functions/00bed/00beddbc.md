# 00beddbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/review-0085.md#review-92ce3807030cf3a4aa6ece279acc2ee5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/review-0042.md#review-92ce3807030cf3a4aa6ece279acc2ee5)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beddbc",
  "name": "FUN_00beddbc",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0e4cbe5139261a7dcf0713b92a00a6b4d988bc649f884444f08214384b14359c",
  "source_text_sha256": "0e4cbe5139261a7dcf0713b92a00a6b4d988bc649f884444f08214384b14359c"
}
~~~

## 呼び出し元

- [00be7110](../00be7/00be7110.md)
- [00bedb1c](../00bed/00bedb1c.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 2090 bytes

~~~c

void FUN_00beddbc(ulong *param_1,ulong *param_2,ulong *param_3,ulong *param_4,ulong *param_5)

{
  ulong uVar1;
  ulong uVar2;
  ulong uVar3;
  
  uVar1 = *param_2;
  uVar2 = *param_1;
  uVar3 = *param_3;
  if (uVar1 < uVar2) {
    if (uVar3 < uVar1) {
      *param_1 = uVar3;
                    /* try { // try from 00bedde0 to 00cedf3b has its CatchHandler @ 00bedde0
                       catch() { ... } // from try @ 00bedde0 with catch @ 00bedde0
                       catch() { ... } // from try @ 00bedf88 with catch @ 00bedde0
                       catch() { ... } // from try @ 00bee064 with catch @ 00bedde0
                       catch() { ... } // from try @ 00bee130 with catch @ 00bedde0
                       catch() { ... } // from try @ 00bee258 with catch @ 00bedde0
                       catch() { ... } // from try @ 00bee4bc with catch @ 00bedde0 */
    }
    else {
      *param_1 = uVar1;
      *param_2 = uVar2;
      uVar3 = *param_3;
      if (uVar2 <= uVar3) goto LAB_00bede3c;
      *param_2 = uVar3;
    }
    *param_3 = uVar2;
    uVar3 = uVar2;
  }
  else if (uVar3 < uVar1) {
    *param_2 = uVar3;
    *param_3 = uVar1;
    uVar2 = *param_1;
    uVar3 = uVar1;
    if (*param_2 < uVar2) {
      *param_1 = *param_2;
      *param_2 = uVar2;
      uVar3 = *param_3;
    }
  }
LAB_00bede3c:
  if (*param_4 < uVar3) {
    *param_3 = *param_4;
    *param_4 = uVar3;
    uVar3 = *param_2;
    if (*param_3 < uVar3) {
      *param_2 = *param_3;
      *param_3 = uVar3;
      uVar3 = *param_1;
      if (*param_2 < uVar3) {
        *param_1 = *param_2;
        *param_2 = uVar3;
      }
    }
  }
  uVar3 = *param_4;
  if (*param_5 < uVar3) {
    *param_4 = *param_5;
    *param_5 = uVar3;
    uVar3 = *param_3;
    if (*param_4 < uVar3) {
      *param_3 = *param_4;
      *param_4 = uVar3;
      uVar3 = *param_2;
      if (*param_3 < uVar3) {
        *param_2 = *param_3;
        *param_3 = uVar3;
        uVar3 = *param_1;
        if (*param_2 < uVar3) {
          *param_1 = *param_2;
          *param_2 = uVar3;
        }
      }
    }
  }
  return;
}

~~~
