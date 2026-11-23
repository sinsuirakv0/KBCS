# 00afc2ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afc374`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc374.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-0d7973028a3787a507ad6ed3ee6d9171)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afc2ac",
  "name": "_ZN8firebase8callback16BlockingCallbackD2Ev",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "be97926dc2869e5c23a11911486bd001b3866818b23978a2b7561dbe6125a4ee",
  "source_text_sha256": "be97926dc2869e5c23a11911486bd001b3866818b23978a2b7561dbe6125a4ee",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afc2ac",
        "00afc2ff"
      ]
    ],
    "bytes_sha256": "0549a4b3a6a0bd67e54262bf0997ef1ff1cd62f8dcd0590a685508dc82b728f7",
    "instruction_count": 21,
    "instruction_bytes": 84,
    "body_bytes": 84,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdebc0](../00bde/00bdebc0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 468 bytes

~~~c

void _ZN8firebase8callback16BlockingCallbackD2Ev(long *param_1)

{
  *param_1 = (long)(PTR__ZTVN8firebase8callback16BlockingCallbackE_00c1b880 + 0x10);
  sem_post(*(sem_t **)param_1[2]);
  if ((long *)param_1[1] != (long *)0x0) {
                    /* WARNING: Could not recover jumptable at 0x00afc2f0. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*(long *)param_1[1] + 8))();
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afc2ac"></a> `00afc2ac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afc2b0"></a> `00afc2b0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afc2b4"></a> `00afc2b4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00afc2b8"></a> `00afc2b8` | `e9 08 00 f0` | adrp x9,0xc1b000 | `FALL_THROUGH`
<a id="insn-00afc2bc"></a> `00afc2bc` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00afc2c0"></a> `00afc2c0` | `29 41 44 f9` | ldr x9,[x9, #0x880] | `FALL_THROUGH`
<a id="insn-00afc2c4"></a> `00afc2c4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afc2c8"></a> `00afc2c8` | `29 41 00 91` | add x9,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00afc2cc"></a> `00afc2cc` | `09 00 00 f9` | str x9,[x0] | `FALL_THROUGH`
<a id="insn-00afc2d0"></a> `00afc2d0` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00afc2d4"></a> `00afc2d4` | `3b 8a 03 94` | bl 0x00bdebc0 | `UNCONDITIONAL_CALL`
<a id="insn-00afc2d8"></a> `00afc2d8` | `60 06 40 f9` | ldr x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00afc2dc"></a> `00afc2dc` | `c0 00 00 b4` | cbz x0,0x00afc2f4 | `CONDITIONAL_JUMP`
<a id="insn-00afc2e0"></a> `00afc2e0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00afc2e4"></a> `00afc2e4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afc2e8"></a> `00afc2e8` | `01 05 40 f9` | ldr x1,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00afc2ec"></a> `00afc2ec` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afc2f0"></a> `00afc2f0` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`
<a id="insn-00afc2f4"></a> `00afc2f4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afc2f8"></a> `00afc2f8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afc2fc"></a> `00afc2fc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afc2ac`](#insn-00afc2ac) 範囲 `[['00afc2ac', '00afc2df']]`
  - `CONDITIONAL_JUMP` [`00afc2dc`](#insn-00afc2dc) → [`00afc2f4`](#insn-00afc2f4)
  - `FALL_THROUGH` [`00afc2dc`](#insn-00afc2dc) → [`00afc2e0`](#insn-00afc2e0)
- ブロック [`00afc2e0`](#insn-00afc2e0) 範囲 `[['00afc2e0', '00afc2f3']]`
- ブロック [`00afc2f4`](#insn-00afc2f4) 範囲 `[['00afc2f4', '00afc2ff']]`

## 命令位置別の参照

- [`00afc2ac`](#insn-00afc2ac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc2b0`](#insn-00afc2b0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc2c0`](#insn-00afc2c0) → `00c1b880`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00afc2cc`](#insn-00afc2cc) → `00c10748`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`00afc2d4`](#insn-00afc2d4) → [`00bdebc0`](../00bde/00bdebc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdebc0` · 推定シンボル `None` · 推定型 `None`
- [`00afc2dc`](#insn-00afc2dc) → [`00afc2f4`](#insn-00afc2f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc2e4`](#insn-00afc2e4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc2f4`](#insn-00afc2f4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afc2ac`](#insn-00afc2ac)

~~~json
{
  "source": "00afc2ac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc2b0`](#insn-00afc2b0)

~~~json
{
  "source": "00afc2b0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc2c0`](#insn-00afc2c0)

~~~json
{
  "source": "00afc2c0",
  "target": "00c1b880",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b880",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00afc2cc`](#insn-00afc2cc)

~~~json
{
  "source": "00afc2cc",
  "target": "00c10748",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10738",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00afc2d4`](#insn-00afc2d4)

~~~json
{
  "source": "00afc2d4",
  "target": "00bdebc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc2dc`](#insn-00afc2dc)

~~~json
{
  "source": "00afc2dc",
  "target": "00afc2f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc2e4`](#insn-00afc2e4)

~~~json
{
  "source": "00afc2e4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc2f4`](#insn-00afc2f4)

~~~json
{
  "source": "00afc2f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
