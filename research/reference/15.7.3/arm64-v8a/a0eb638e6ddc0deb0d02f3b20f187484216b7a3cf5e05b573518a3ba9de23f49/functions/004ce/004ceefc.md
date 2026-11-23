# 004ceefc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `004ceefc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ceefc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/detail_skipped-0003.md#compare-ae77323a514f6adebee8a47ceb526a82)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004ceefc",
  "name": "_ZTv0_n48_NK5Botan13RSA_PublicKey10key_lengthEv",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "92248f85f662ab74872ab39c16b2673522112b2972c0a2769e08f902d35e4057",
  "source_text_sha256": "92248f85f662ab74872ab39c16b2673522112b2972c0a2769e08f902d35e4057"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 899 bytes

~~~c

long _ZTv0_n48_NK5Botan13RSA_PublicKey10key_lengthEv(long *param_1)

{
  long lVar1;
  uint uVar2;
  ulong uVar3;
  ulong uVar4;
  long lVar5;
  
  lVar5 = *(long *)((long)param_1 + *(long *)(*param_1 + -0x30) + 8);
  lVar1 = *(long *)((long)param_1 + *(long *)(*param_1 + -0x30) + 0x10) - lVar5;
  uVar3 = lVar1 >> 2;
  uVar4 = uVar3;
  if (lVar1 == 0) {
LAB_004cef38:
    if (uVar4 != 0) {
      uVar4 = uVar4 - 1;
      if (uVar4 < uVar3) {
        uVar2 = *(uint *)(lVar5 + uVar4 * 4);
      }
      else {
        uVar2 = 0;
      }
      lVar5 = 0x20;
      do {
        if ((uVar2 >> (ulong)((int)lVar5 - 1U & 0x1f) & 1) != 0) break;
        lVar5 = lVar5 + -1;
      } while (lVar5 != 0);
      return lVar5 + uVar4 * 0x20;
    }
  }
  else {
    do {
      if (*(int *)(lVar5 + -4 + uVar4 * 4) != 0) goto LAB_004cef38;
      uVar4 = uVar4 - 1;
    } while (uVar4 != 0);
  }
  return 0;
}

~~~
