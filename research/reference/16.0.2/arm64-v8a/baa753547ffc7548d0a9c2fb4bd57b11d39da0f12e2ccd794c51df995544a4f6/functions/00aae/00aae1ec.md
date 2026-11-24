# 00aae1ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aae17c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aae/00aae17c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0064.md#compare-e5847ff9b77246716f85f3cc84123332)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0028.md#compare-bf45e6a0440cee6004036873728d6722)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aae1ec",
  "name": "FUN_00aae1ec",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a71cfc6bcaf16474761eb200bbcb20d3f936234a1ffcf1fd4e2836bd3f78c903",
  "source_text_sha256": "a71cfc6bcaf16474761eb200bbcb20d3f936234a1ffcf1fd4e2836bd3f78c903"
}
~~~

## 呼び出し元

- [00aa5998](../00aa5/00aa5998.md)
- [00aa6150](../00aa6/00aa6150.md)
- [00aae1ec](../00aae/00aae1ec.md)

## 呼び出し先

- [005b9f24](../005b9/005b9f24.md)
- [00aae1ec](../00aae/00aae1ec.md)
- [00c57f80](../00c57/00c57f80.md)

## 疑似コード / UTF-8 266 bytes

~~~c

void FUN_00aae1ec(undefined8 param_1,undefined8 *param_2)

{
  if (param_2 != (undefined8 *)0x0) {
    FUN_00aae1ec(param_1,*param_2);
    FUN_00aae1ec(param_1,param_2[1]);
    FUN_005b9f24(param_2 + 5,param_2[6]);
    _ZdlPv(param_2);
    return;
  }
  return;
}

~~~
