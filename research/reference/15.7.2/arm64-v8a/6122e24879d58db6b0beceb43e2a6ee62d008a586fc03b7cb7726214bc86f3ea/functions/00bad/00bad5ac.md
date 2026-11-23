# 00bad5ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bad674`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad674.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-4b2062255cdc9587db99d85d913bf9ad)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bad5ac",
  "name": "_ZNKSt6__ndk114__codecvt_utf8IDiE6do_outER9mbstate_tPKDiS5_RS5_PcS7_RS7_",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e80eba9b6bace175169721e8d134ed2d989e542938cef1b21b11f4ea2d64cc6d",
  "source_text_sha256": "e80eba9b6bace175169721e8d134ed2d989e542938cef1b21b11f4ea2d64cc6d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bad5ac",
        "00bad61b"
      ]
    ],
    "bytes_sha256": "ccbbe2f57ae50536023c1faa01cd0ca6db4433aa71615831a9cb64444f781ac0",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bac7a8](../00bac/00bac7a8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 568 bytes

~~~c

void _ZNKSt6__ndk114__codecvt_utf8IDiE6do_outER9mbstate_tPKDiS5_RS5_PcS7_RS7_
               (long param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 *param_5,undefined8 param_6,undefined8 param_7,undefined8 *param_8)

{
  undefined8 local_30;
  undefined8 uStack_28;
  
  local_30 = param_6;
  uStack_28 = param_3;
  FUN_00bac7a8(param_3,param_4,&uStack_28,param_6,param_7,&local_30,*(undefined8 *)(param_1 + 0x10),
               *(undefined4 *)(param_1 + 0x18));
  *param_5 = uStack_28;
  *param_8 = local_30;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bad5ac"></a> `00bad5ac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bad5b0"></a> `00bad5b0` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bad5b4"></a> `00bad5b4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bad5b8"></a> `00bad5b8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bad5bc"></a> `00bad5bc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bad5c0"></a> `00bad5c0` | `f3 03 07 aa` | mov x19,x7 | `FALL_THROUGH`
<a id="insn-00bad5c4"></a> `00bad5c4` | `ea 03 06 aa` | mov x10,x6 | `FALL_THROUGH`
<a id="insn-00bad5c8"></a> `00bad5c8` | `e8 03 05 aa` | mov x8,x5 | `FALL_THROUGH`
<a id="insn-00bad5cc"></a> `00bad5cc` | `e9 03 02 aa` | mov x9,x2 | `FALL_THROUGH`
<a id="insn-00bad5d0"></a> `00bad5d0` | `06 08 40 f9` | ldr x6,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bad5d4"></a> `00bad5d4` | `07 18 40 b9` | ldr w7,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bad5d8"></a> `00bad5d8` | `f4 03 04 aa` | mov x20,x4 | `FALL_THROUGH`
<a id="insn-00bad5dc"></a> `00bad5dc` | `e1 03 03 aa` | mov x1,x3 | `FALL_THROUGH`
<a id="insn-00bad5e0"></a> `00bad5e0` | `e5 0b 00 a9` | stp x5,x2,[sp] | `FALL_THROUGH`
<a id="insn-00bad5e4"></a> `00bad5e4` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bad5e8"></a> `00bad5e8` | `e5 03 00 91` | mov x5,sp | `FALL_THROUGH`
<a id="insn-00bad5ec"></a> `00bad5ec` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-00bad5f0"></a> `00bad5f0` | `e3 03 08 aa` | mov x3,x8 | `FALL_THROUGH`
<a id="insn-00bad5f4"></a> `00bad5f4` | `e4 03 0a aa` | mov x4,x10 | `FALL_THROUGH`
<a id="insn-00bad5f8"></a> `00bad5f8` | `6c fc ff 97` | bl 0x00bac7a8 | `UNCONDITIONAL_CALL`
<a id="insn-00bad5fc"></a> `00bad5fc` | `e9 23 40 a9` | ldp x9,x8,[sp] | `FALL_THROUGH`
<a id="insn-00bad600"></a> `00bad600` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00bad604"></a> `00bad604` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00bad608"></a> `00bad608` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bad60c"></a> `00bad60c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bad610"></a> `00bad610` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bad614"></a> `00bad614` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bad618"></a> `00bad618` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bad5ac`](#insn-00bad5ac) 範囲 `[['00bad5ac', '00bad61b']]`

## 命令位置別の参照

- [`00bad5b4`](#insn-00bad5b4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad5b8`](#insn-00bad5b8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad5e0`](#insn-00bad5e0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad5f8`](#insn-00bad5f8) → [`00bac7a8`](../00bac/00bac7a8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bac7a8` · 推定シンボル `None` · 推定型 `None`
- [`00bad5fc`](#insn-00bad5fc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad608`](#insn-00bad608) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad60c`](#insn-00bad60c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bad5b4`](#insn-00bad5b4)

~~~json
{
  "source": "00bad5b4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad5b8`](#insn-00bad5b8)

~~~json
{
  "source": "00bad5b8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad5e0`](#insn-00bad5e0)

~~~json
{
  "source": "00bad5e0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad5f8`](#insn-00bad5f8)

~~~json
{
  "source": "00bad5f8",
  "target": "00bac7a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad5fc`](#insn-00bad5fc)

~~~json
{
  "source": "00bad5fc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad608`](#insn-00bad608)

~~~json
{
  "source": "00bad608",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad60c`](#insn-00bad60c)

~~~json
{
  "source": "00bad60c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
