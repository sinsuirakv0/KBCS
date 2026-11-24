# 00aefac8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aefa2c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aefa2c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0066.md#compare-58be251b59c09e7b7bbcd50ec2d7b7da)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0077.md#compare-902659b7eb045df32f3541c9cde79c60)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aefac8",
  "name": "FUN_00aefac8",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e03d5ab5ee8e70d7158562d2405ae134db6b0ca87d6f8f2c556a7ae6763ef98d",
  "source_text_sha256": "e03d5ab5ee8e70d7158562d2405ae134db6b0ca87d6f8f2c556a7ae6763ef98d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [008b6ab4](../008b6/008b6ab4.md)
- [008b6f68](../008b6/008b6f68.md)
- [008b7a20](../008b7/008b7a20.md)

## 疑似コード / UTF-8 193 bytes

~~~c

void FUN_00aefac8(long param_1)

{
  undefined8 uVar1;
  
  uVar1 = FUN_008b7a20(*(long *)(param_1 + 8) + 0x2f38,0x326);
  uVar1 = FUN_008b6f68(uVar1,1);
  FUN_008b6ab4(uVar1,0);
  return;
}

~~~
