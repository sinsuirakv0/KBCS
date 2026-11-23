# 00adfa7c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adfb44`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adfb44.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0001.md#compare-156d2b024fda5a2c015821086c152f3e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adfa7c",
  "name": "FUN_00adfa7c",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "991eb2ec41a54801d21e11a981c677893e3332db7b02e0317b3a4633c203f284",
  "source_text_sha256": "991eb2ec41a54801d21e11a981c677893e3332db7b02e0317b3a4633c203f284",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adfa7c",
        "00adfaaf"
      ]
    ],
    "bytes_sha256": "ab0e36523b4d62ba9d73ec706647d903f75b8c86b9d479a8be74d7be1253e2b1",
    "instruction_count": 13,
    "instruction_bytes": 52,
    "body_bytes": 52,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 418 bytes

~~~c

void FUN_00adfa7c(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
                    /* try { // try from 00adfa80 to 00bdfa87 has its CatchHandler @ 00adfc30 */
  puVar1 = (undefined8 *)_Znwm(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
                    /* try { // try from 00adfa98 to 00bdfa9f has its CatchHandler @ 00adfc14 */
  *puVar1 = &PTR_FUN_00c0f948;
  puVar1[1] = uVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00adfa7c"></a> `00adfa7c` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00adfa80"></a> `00adfa80` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adfa84"></a> `00adfa84` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00adfa88"></a> `00adfa88` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00adfa8c"></a> `00adfa8c` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00adfa90"></a> `00adfa90` | `2c ed 03 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00adfa94"></a> `00adfa94` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00adfa98"></a> `00adfa98` | `88 09 00 90` | adrp x8,0xc0f000 | `FALL_THROUGH`
<a id="insn-00adfa9c"></a> `00adfa9c` | `08 21 25 91` | add x8,x8,#0x948 | `FALL_THROUGH`
<a id="insn-00adfaa0"></a> `00adfaa0` | `08 24 00 a9` | stp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00adfaa4"></a> `00adfaa4` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adfaa8"></a> `00adfaa8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00adfaac"></a> `00adfaac` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adfa7c`](#insn-00adfa7c) 範囲 `[['00adfa7c', '00adfa7f']]`
  - `FALL_THROUGH` [`00adfa7c`](#insn-00adfa7c) → [`00adfa80`](#insn-00adfa80)
- ブロック [`00adfa80`](#insn-00adfa80) 範囲 `[['00adfa80', '00adfa97']]`
  - `FALL_THROUGH` [`00adfa94`](#insn-00adfa94) → [`00adfa98`](#insn-00adfa98)
- ブロック [`00adfa98`](#insn-00adfa98) 範囲 `[['00adfa98', '00adfaaf']]`

## 命令位置別の参照

- [`00adfa7c`](#insn-00adfa7c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfa80`](#insn-00adfa80) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfa90`](#insn-00adfa90) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00adfaa0`](#insn-00adfaa0) → `00c0f948`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00adfaa4`](#insn-00adfaa4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfaa8`](#insn-00adfaa8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adfa7c`](#insn-00adfa7c)

~~~json
{
  "source": "00adfa7c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfa80`](#insn-00adfa80)

~~~json
{
  "source": "00adfa80",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfa90`](#insn-00adfa90)

~~~json
{
  "source": "00adfa90",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfaa0`](#insn-00adfaa0)

~~~json
{
  "source": "00adfaa0",
  "target": "00c0f948",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f948",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00adfaa4`](#insn-00adfaa4)

~~~json
{
  "source": "00adfaa4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfaa8`](#insn-00adfaa8)

~~~json
{
  "source": "00adfaa8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
