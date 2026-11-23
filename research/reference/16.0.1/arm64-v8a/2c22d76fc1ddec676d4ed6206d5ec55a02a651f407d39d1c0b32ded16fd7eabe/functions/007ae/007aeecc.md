# 007aeecc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `007aee8c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aee8c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0038.md#compare-8982ed257522cdd5164374dfec560820)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0041.md#compare-68c5e25a645480b7ea0081020684b08d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007aeecc",
  "name": "FUN_007aeecc",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eba589f2cdcd30c10f97306385f911ab1347f9bc439f0abfcab593a1a28fab0f",
  "source_text_sha256": "eba589f2cdcd30c10f97306385f911ab1347f9bc439f0abfcab593a1a28fab0f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0043bb20](../0043b/0043bb20.md)

## 疑似コード / UTF-8 568 bytes

~~~c

void FUN_007aeecc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  *param_2 = &PTR_FUN_00c7a718;
  if ((*(byte *)(param_1 + 8) & 1) == 0) {
    uVar2 = *(undefined8 *)(param_1 + 0x10);
    uVar1 = *(undefined8 *)(param_1 + 8);
    param_2[3] = *(undefined8 *)(param_1 + 0x18);
                    /* catch() { ... } // from try @ 007ae04c with catch @ 007aeef0 */
    param_2[2] = uVar2;
    param_2[1] = uVar1;
    return;
  }
  FUN_0043bb20(param_2 + 1,*(undefined8 *)(param_1 + 0x18),*(undefined8 *)(param_1 + 0x10));
  return;
}

~~~
