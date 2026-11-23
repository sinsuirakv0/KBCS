# 00adbf5c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adc024`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc024.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-454b4bfbdcf094d295b171bf0cb99296)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adbf5c",
  "name": "FUN_00adbf5c",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b18325893aa22436b32d54703741eb4d8b8d3a3be3af589e917f5221c3212903",
  "source_text_sha256": "b18325893aa22436b32d54703741eb4d8b8d3a3be3af589e917f5221c3212903",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adbf5c",
        "00adbf87"
      ]
    ],
    "bytes_sha256": "f40e7be02f686f1607059bb60225872b6d46c15b9e872c13b2d861eb5cb71f6a",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0080dd1c](../0080d/0080dd1c.md)
- [00814828](../00814/00814828.md)

## 呼び出し先

- [005c3468](../005c3/005c3468.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 131 bytes

~~~c

void FUN_00adbf5c(undefined4 *param_1)

{
  *param_1 = 0;
  FUN_005c3468();
  *param_1 = 0;
  FUN_005c3468(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00adbf5c"></a> `00adbf5c` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00adbf60"></a> `00adbf60` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adbf64"></a> `00adbf64` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00adbf68"></a> `00adbf68` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00adbf6c"></a> `00adbf6c` | `1f 00 00 b9` | str wzr,[x0] | `FALL_THROUGH`
<a id="insn-00adbf70"></a> `00adbf70` | `3e 9d eb 97` | bl 0x005c3468 | `UNCONDITIONAL_CALL`
<a id="insn-00adbf74"></a> `00adbf74` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adbf78"></a> `00adbf78` | `7f 02 00 b9` | str wzr,[x19] | `FALL_THROUGH`
<a id="insn-00adbf7c"></a> `00adbf7c` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adbf80"></a> `00adbf80` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00adbf84"></a> `00adbf84` | `39 9d eb 17` | b 0x005c3468 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adbf5c`](#insn-00adbf5c) 範囲 `[['00adbf5c', '00adbf87']]`

## 命令位置別の参照

- [`00adbf5c`](#insn-00adbf5c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbf60`](#insn-00adbf60) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbf70`](#insn-00adbf70) → [`005c3468`](../005c3/005c3468.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c3468` · 推定シンボル `None` · 推定型 `None`
- [`00adbf7c`](#insn-00adbf7c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbf80`](#insn-00adbf80) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbf84`](#insn-00adbf84) → [`005c3468`](../005c3/005c3468.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c3468` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adbf5c`](#insn-00adbf5c)

~~~json
{
  "source": "00adbf5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbf60`](#insn-00adbf60)

~~~json
{
  "source": "00adbf60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbf70`](#insn-00adbf70)

~~~json
{
  "source": "00adbf70",
  "target": "005c3468",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbf7c`](#insn-00adbf7c)

~~~json
{
  "source": "00adbf7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbf80`](#insn-00adbf80)

~~~json
{
  "source": "00adbf80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbf84`](#insn-00adbf84)

~~~json
{
  "source": "00adbf84",
  "target": "005c3468",
  "target_space": "ram",
  "resolution": "function"
}
~~~
