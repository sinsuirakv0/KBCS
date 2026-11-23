# 009dfdac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `009dfc10`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009dfc10.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0032.md#compare-3321426f6d042b3ef56d9f1c1dd4d2bd)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0032.md#compare-dc0354fa57f5f0d7e798dfade3f1e7bf)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009dfdac",
  "name": "FUN_009dfdac",
  "size": 96,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df6dc82b76bdef2cca79aa2572a4787c1d0144aae74bfc68abba5809326f2fc8",
  "source_text_sha256": "df6dc82b76bdef2cca79aa2572a4787c1d0144aae74bfc68abba5809326f2fc8"
}
~~~

## 呼び出し元

- [00ad0958](../00ad0/00ad0958.md)

## 呼び出し先

- [005c179c](../005c1/005c179c.md)
- [009dfb18](../009df/009dfb18.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 419 bytes

~~~c

bool FUN_009dfdac(void)

{
  long lVar1;
  undefined1 auStack_40 [8];
  undefined8 local_38;
  ulong uStack_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  FUN_009dfb18(auStack_40);
  FUN_005c179c(auStack_40,local_38);
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return 1 < uStack_30;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
