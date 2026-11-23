# 00b7cfbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b7d084`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d084.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0074.md#compare-77a7af201fc0d0c3a09bc9a966792f09)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b7cfbc",
  "name": "_ZNSt6__ndk17promiseIvE24set_value_at_thread_exitEv",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "428e69339109ed2e4f09cee9abe5300c2d3b3cc01d1d144a2b3e79c12cef92c8",
  "source_text_sha256": "428e69339109ed2e4f09cee9abe5300c2d3b3cc01d1d144a2b3e79c12cef92c8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b7cfbc",
        "00b7cfdf"
      ]
    ],
    "bytes_sha256": "e883f3ce7e8d6c2c1949e19bf36b85eaa9afddfd51221fb33454f991173e2292",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [004377fc](../00437/004377fc.md)
- [00be1120](../00be1/00be1120.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 363 bytes

~~~c

void _ZNSt6__ndk17promiseIvE24set_value_at_thread_exitEv(long *param_1)

{
  if (*param_1 != 0) {
    _ZNSt6__ndk117__assoc_sub_state24set_value_at_thread_exitEv();
    return;
  }
                    /* try { // try from 00b7cfd0 to 00c7d023 has its CatchHandler @ 00b7888c */
                    /* WARNING: Subroutine does not return */
  FUN_004377fc(3);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b7cfbc"></a> `00b7cfbc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00b7cfc0"></a> `00b7cfc0` | `00 00 40 f9` | ldr x0,[x0] | `FALL_THROUGH`
<a id="insn-00b7cfc4"></a> `00b7cfc4` | `40 00 00 b4` | cbz x0,0x00b7cfcc | `CONDITIONAL_JUMP`
<a id="insn-00b7cfc8"></a> `00b7cfc8` | `56 90 01 14` | b 0x00be1120 | `CALL_TERMINATOR`
<a id="insn-00b7cfcc"></a> `00b7cfcc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00b7cfd0"></a> `00b7cfd0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00b7cfd4"></a> `00b7cfd4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b7cfd8"></a> `00b7cfd8` | `60 00 80 52` | mov w0,#0x3 | `FALL_THROUGH`
<a id="insn-00b7cfdc"></a> `00b7cfdc` | `08 ea e2 97` | bl 0x004377fc | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b7cfbc`](#insn-00b7cfbc) 範囲 `[['00b7cfbc', '00b7cfc7']]`
  - `CONDITIONAL_JUMP` [`00b7cfc4`](#insn-00b7cfc4) → [`00b7cfcc`](#insn-00b7cfcc)
  - `FALL_THROUGH` [`00b7cfc4`](#insn-00b7cfc4) → [`00b7cfc8`](#insn-00b7cfc8)
- ブロック [`00b7cfc8`](#insn-00b7cfc8) 範囲 `[['00b7cfc8', '00b7cfcb']]`
- ブロック [`00b7cfcc`](#insn-00b7cfcc) 範囲 `[['00b7cfcc', '00b7cfcf']]`
  - `FALL_THROUGH` [`00b7cfcc`](#insn-00b7cfcc) → [`00b7cfd0`](#insn-00b7cfd0)
- ブロック [`00b7cfd0`](#insn-00b7cfd0) 範囲 `[['00b7cfd0', '00b7cfdf']]`

## 命令位置別の参照

- [`00b7cfc4`](#insn-00b7cfc4) → [`00b7cfcc`](#insn-00b7cfcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cfc8`](#insn-00b7cfc8) → [`00be1120`](../00be1/00be1120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1120` · 推定シンボル `None` · 推定型 `None`
- [`00b7cfd0`](#insn-00b7cfd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cfdc`](#insn-00b7cfdc) → [`004377fc`](../00437/004377fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004377fc` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b7cfc4`](#insn-00b7cfc4)

~~~json
{
  "source": "00b7cfc4",
  "target": "00b7cfcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cfc8`](#insn-00b7cfc8)

~~~json
{
  "source": "00b7cfc8",
  "target": "00be1120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7cfd0`](#insn-00b7cfd0)

~~~json
{
  "source": "00b7cfd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cfdc`](#insn-00b7cfdc)

~~~json
{
  "source": "00b7cfdc",
  "target": "004377fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
