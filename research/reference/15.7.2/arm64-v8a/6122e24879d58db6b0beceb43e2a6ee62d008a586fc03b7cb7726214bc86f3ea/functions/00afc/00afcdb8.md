# 00afcdb8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afce80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afce80.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0063.md#compare-7973f960b2178bc31dad6cbff5a8e07e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afcdb8",
  "name": "_INIT_273",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d506302ef376401ac49ad7ee34fb2d0f6cf3bd7c6532c48bf713383b5003cdf7",
  "source_text_sha256": "d506302ef376401ac49ad7ee34fb2d0f6cf3bd7c6532c48bf713383b5003cdf7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afcdb8",
        "00afcdef"
      ]
    ],
    "bytes_sha256": "c9413828d87ea4c7ff2065e4e2118b1122cfeeddf1a2b1c113725f24f75b8582",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00bddd20](../00bdd/00bddd20.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 434 bytes

~~~c

void _INIT_273(void)

{
  undefined8 uVar1;
  
                    /* try { // try from 00afcdc8 to 00bfcddf has its CatchHandler @ 00aff3b8 */
  uVar1 = _Znwm(0x28);
  _ZN8firebase5MutexC2ENS0_4ModeE(uVar1,1);
                    /* try { // try from 00afcde0 to 00bfce7b has its CatchHandler @ 00af560c */
  *(undefined8 *)PTR__ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E_00c1b898 =
       uVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afcdb8"></a> `00afcdb8` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afcdbc"></a> `00afcdbc` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcdc0"></a> `00afcdc0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00afcdc4"></a> `00afcdc4` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00afcdc8"></a> `00afcdc8` | `5e 78 03 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00afcdcc"></a> `00afcdcc` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00afcdd0"></a> `00afcdd0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afcdd4"></a> `00afcdd4` | `d3 83 03 94` | bl 0x00bddd20 | `UNCONDITIONAL_CALL`
<a id="insn-00afcdd8"></a> `00afcdd8` | `e8 08 00 f0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00afcddc"></a> `00afcddc` | `08 4d 44 f9` | ldr x8,[x8, #0x898] | `FALL_THROUGH`
<a id="insn-00afcde0"></a> `00afcde0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcde4"></a> `00afcde4` | `13 01 00 f9` | str x19,[x8] | `FALL_THROUGH`
<a id="insn-00afcde8"></a> `00afcde8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afcdec"></a> `00afcdec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afcdb8`](#insn-00afcdb8) 範囲 `[['00afcdb8', '00afcdc7']]`
  - `FALL_THROUGH` [`00afcdc4`](#insn-00afcdc4) → [`00afcdc8`](#insn-00afcdc8)
- ブロック [`00afcdc8`](#insn-00afcdc8) 範囲 `[['00afcdc8', '00afcddf']]`
  - `FALL_THROUGH` [`00afcddc`](#insn-00afcddc) → [`00afcde0`](#insn-00afcde0)
- ブロック [`00afcde0`](#insn-00afcde0) 範囲 `[['00afcde0', '00afcdef']]`

## 命令位置別の参照

- [`00afcdb8`](#insn-00afcdb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcdbc`](#insn-00afcdbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcdc8`](#insn-00afcdc8) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00afcdd4`](#insn-00afcdd4) → [`00bddd20`](../00bdd/00bddd20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddd20` · 推定シンボル `None` · 推定型 `None`
- [`00afcddc`](#insn-00afcddc) → `00c1b898`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00afcde0`](#insn-00afcde0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcde4`](#insn-00afcde4) → `010a0c48`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E` · 推定型 `undefined8`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afcdb8`](#insn-00afcdb8)

~~~json
{
  "source": "00afcdb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcdbc`](#insn-00afcdbc)

~~~json
{
  "source": "00afcdbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcdc8`](#insn-00afcdc8)

~~~json
{
  "source": "00afcdc8",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcdd4`](#insn-00afcdd4)

~~~json
{
  "source": "00afcdd4",
  "target": "00bddd20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcddc`](#insn-00afcddc)

~~~json
{
  "source": "00afcddc",
  "target": "00c1b898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b898",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00afcde0`](#insn-00afcde0)

~~~json
{
  "source": "00afcde0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcde4`](#insn-00afcde4)

~~~json
{
  "source": "00afcde4",
  "target": "010a0c48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0c48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
