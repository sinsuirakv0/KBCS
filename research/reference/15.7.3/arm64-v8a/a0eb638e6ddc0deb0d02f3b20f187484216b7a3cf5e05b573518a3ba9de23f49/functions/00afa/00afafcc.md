# 00afafcc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00afaf04`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afaf04.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-bc3b6d22a22b5cb9f38a61085797cce2)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afb010`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb010.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0066.md#compare-550f3e6f88b42be37dac9a40a00a7ff5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afafcc",
  "name": "_INIT_271",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "99ca1c56ae997c87c1621e448ad027399344cd97eee07db8c093eb81d060ba92",
  "source_text_sha256": "99ca1c56ae997c87c1621e448ad027399344cd97eee07db8c093eb81d060ba92",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afafcc",
        "00afb01b"
      ]
    ],
    "bytes_sha256": "93db0c184a38f5a95d09d7c0f8b1e88ae4d6c238ee5744423846c71831291b1f",
    "instruction_count": 20,
    "instruction_bytes": 80,
    "body_bytes": 80,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf90](../00bda/00bdaf90.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdddd0](../00bdd/00bdddd0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 491 bytes

~~~c

void _INIT_271(void)

{
  undefined8 uVar1;
  
                    /* try { // try from 00afafd4 to 00bfafdb has its CatchHandler @ 00aff4d4 */
  __cxa_atexit(PTR__ZN8firebase6LoggerD2Ev_00c1b8a0,
               PTR__ZN8firebase10app_common15g_system_loggerE_00c1b908,&PTR_LOOP_00be5f80);
  uVar1 = _Znwm(0x28);
                    /* try { // try from 00afb004 to 00bfb017 has its CatchHandler @ 00aff4d0 */
  _ZN8firebase5MutexC2ENS0_4ModeE(uVar1,1);
  DAT_010a0cc0 = uVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afafcc"></a> `00afafcc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afafd0"></a> `00afafd0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afafd4"></a> `00afafd4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00afafd8"></a> `00afafd8` | `00 09 00 b0` | adrp x0,0xc1b000 | `FALL_THROUGH`
<a id="insn-00afafdc"></a> `00afafdc` | `01 09 00 b0` | adrp x1,0xc1b000 | `FALL_THROUGH`
<a id="insn-00afafe0"></a> `00afafe0` | `00 50 44 f9` | ldr x0,[x0, #0x8a0] | `FALL_THROUGH`
<a id="insn-00afafe4"></a> `00afafe4` | `21 84 44 f9` | ldr x1,[x1, #0x908] | `FALL_THROUGH`
<a id="insn-00afafe8"></a> `00afafe8` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00afafec"></a> `00afafec` | `a2 7c 75 10` | adr x2,0xbe5f80 | `FALL_THROUGH`
<a id="insn-00afaff0"></a> `00afaff0` | `e8 7f 03 94` | bl 0x00bdaf90 | `UNCONDITIONAL_CALL`
<a id="insn-00afaff4"></a> `00afaff4` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00afaff8"></a> `00afaff8` | `fe 7f 03 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00afaffc"></a> `00afaffc` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00afb000"></a> `00afb000` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afb004"></a> `00afb004` | `73 8b 03 94` | bl 0x00bdddd0 | `UNCONDITIONAL_CALL`
<a id="insn-00afb008"></a> `00afb008` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afb00c"></a> `00afb00c` | `28 2d 00 b0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00afb010"></a> `00afb010` | `13 61 06 f9` | str x19,[x8, #0xcc0] | `FALL_THROUGH`
<a id="insn-00afb014"></a> `00afb014` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afb018"></a> `00afb018` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afafcc`](#insn-00afafcc) 範囲 `[['00afafcc', '00afafd3']]`
  - `FALL_THROUGH` [`00afafd0`](#insn-00afafd0) → [`00afafd4`](#insn-00afafd4)
- ブロック [`00afafd4`](#insn-00afafd4) 範囲 `[['00afafd4', '00afb003']]`
  - `FALL_THROUGH` [`00afb000`](#insn-00afb000) → [`00afb004`](#insn-00afb004)
- ブロック [`00afb004`](#insn-00afb004) 範囲 `[['00afb004', '00afb01b']]`

## 命令位置別の参照

- [`00afafcc`](#insn-00afafcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afafd0`](#insn-00afafd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afafe0`](#insn-00afafe0) → `00c1b8a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00afafe0`](#insn-00afafe0) → [`00afb01c`](../00afb/00afb01c.md) · `PARAM` · `ANALYSIS` · 関数 `00afb01c` · 推定シンボル `_ZN8firebase6LoggerD2Ev` · 推定型 `None`
- [`00afafe4`](#insn-00afafe4) → `00c1b908`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00afafe4`](#insn-00afafe4) → `00c24750`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase10app_common15g_system_loggerE` · 推定型 `pointer __((offset(0x10)))`
- [`00afafec`](#insn-00afafec) → `00be5f80`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00afaff0`](#insn-00afaff0) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`
- [`00afaff8`](#insn-00afaff8) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00afb004`](#insn-00afb004) → [`00bdddd0`](../00bdd/00bdddd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdddd0` · 推定シンボル `None` · 推定型 `None`
- [`00afb008`](#insn-00afb008) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb010`](#insn-00afb010) → `010a0cc0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afafcc`](#insn-00afafcc)

~~~json
{
  "source": "00afafcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afafd0`](#insn-00afafd0)

~~~json
{
  "source": "00afafd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afafe0`](#insn-00afafe0)

~~~json
{
  "source": "00afafe0",
  "target": "00c1b8a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b8a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00afafe0`](#insn-00afafe0)

~~~json
{
  "source": "00afafe0",
  "target": "00afb01c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afafe4`](#insn-00afafe4)

~~~json
{
  "source": "00afafe4",
  "target": "00c1b908",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b908",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00afafe4`](#insn-00afafe4)

~~~json
{
  "source": "00afafe4",
  "target": "00c24750",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24750",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00afafec`](#insn-00afafec)

~~~json
{
  "source": "00afafec",
  "target": "00be5f80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be5f80",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00afaff0`](#insn-00afaff0)

~~~json
{
  "source": "00afaff0",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaff8`](#insn-00afaff8)

~~~json
{
  "source": "00afaff8",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb004`](#insn-00afb004)

~~~json
{
  "source": "00afb004",
  "target": "00bdddd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb008`](#insn-00afb008)

~~~json
{
  "source": "00afb008",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb010`](#insn-00afb010)

~~~json
{
  "source": "00afb010",
  "target": "010a0cc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0cc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
