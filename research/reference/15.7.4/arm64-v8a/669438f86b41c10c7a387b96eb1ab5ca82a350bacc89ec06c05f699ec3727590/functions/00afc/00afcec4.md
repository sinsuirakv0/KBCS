# 00afcec4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afce80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afce80.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0008.md#compare-8349615a16dee2126080fb89ee4907d4)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0090.md#review-587f996157922ea639f225ec15e1254b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afcec4",
  "name": "_INIT_273",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ed2407d1fecac19070c8fa3707bcafd87a42391a30f22b0ad0fed4214b1af04e",
  "source_text_sha256": "ed2407d1fecac19070c8fa3707bcafd87a42391a30f22b0ad0fed4214b1af04e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afcec4",
        "00afcefb"
      ]
    ],
    "bytes_sha256": "96188983267d4b174c6797e41db5d001e65bdc44538ee900518b9b74e59ed12a",
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

- [00bdb040](../00bdb/00bdb040.md)
- [00bdde20](../00bdd/00bdde20.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 337 bytes

~~~c

void _INIT_273(void)

{
  undefined8 uVar1;
  
  uVar1 = _Znwm(0x28);
  _ZN8firebase5MutexC2ENS0_4ModeE(uVar1,1);
                    /* try { // try from 00afcef0 to 00bfcf07 has its CatchHandler @ 00aff3f0 */
  *(undefined8 *)PTR__ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E_00c1b998 =
       uVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afcec4"></a> `00afcec4` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afcec8"></a> `00afcec8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcecc"></a> `00afcecc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00afced0"></a> `00afced0` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00afced4"></a> `00afced4` | `5b 78 03 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00afced8"></a> `00afced8` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00afcedc"></a> `00afcedc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afcee0"></a> `00afcee0` | `d0 83 03 94` | bl 0x00bdde20 | `UNCONDITIONAL_CALL`
<a id="insn-00afcee4"></a> `00afcee4` | `e8 08 00 f0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00afcee8"></a> `00afcee8` | `08 cd 44 f9` | ldr x8,[x8, #0x998] | `FALL_THROUGH`
<a id="insn-00afceec"></a> `00afceec` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcef0"></a> `00afcef0` | `13 01 00 f9` | str x19,[x8] | `FALL_THROUGH`
<a id="insn-00afcef4"></a> `00afcef4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afcef8"></a> `00afcef8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afcec4`](#insn-00afcec4) 範囲 `[['00afcec4', '00afceef']]`
  - `FALL_THROUGH` [`00afceec`](#insn-00afceec) → [`00afcef0`](#insn-00afcef0)
- ブロック [`00afcef0`](#insn-00afcef0) 範囲 `[['00afcef0', '00afcefb']]`

## 命令位置別の参照

- [`00afcec4`](#insn-00afcec4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcec8`](#insn-00afcec8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afced4`](#insn-00afced4) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00afcee0`](#insn-00afcee0) → [`00bdde20`](../00bdd/00bdde20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdde20` · 推定シンボル `None` · 推定型 `None`
- [`00afcee8`](#insn-00afcee8) → `00c1b998`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00afceec`](#insn-00afceec) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcef0`](#insn-00afcef0) → `010a0d48`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E` · 推定型 `undefined8`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afcec4`](#insn-00afcec4)

~~~json
{
  "source": "00afcec4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcec8`](#insn-00afcec8)

~~~json
{
  "source": "00afcec8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afced4`](#insn-00afced4)

~~~json
{
  "source": "00afced4",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcee0`](#insn-00afcee0)

~~~json
{
  "source": "00afcee0",
  "target": "00bdde20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcee8`](#insn-00afcee8)

~~~json
{
  "source": "00afcee8",
  "target": "00c1b998",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b998",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00afceec`](#insn-00afceec)

~~~json
{
  "source": "00afceec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcef0`](#insn-00afcef0)

~~~json
{
  "source": "00afcef0",
  "target": "010a0d48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0d48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
