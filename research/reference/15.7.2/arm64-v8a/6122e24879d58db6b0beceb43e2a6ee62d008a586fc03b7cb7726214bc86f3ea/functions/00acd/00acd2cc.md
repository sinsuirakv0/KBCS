# 00acd2cc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00acd394`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd394.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-bc0629a036944166d76c728dd0ea991c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acd2cc",
  "name": "FUN_00acd2cc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3d2c3139844e6c8dcdac4995e606bd00dedd25f8ace65487de7c1705b66768fe",
  "source_text_sha256": "3d2c3139844e6c8dcdac4995e606bd00dedd25f8ace65487de7c1705b66768fe",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acd2cc",
        "00acd313"
      ]
    ],
    "bytes_sha256": "263918e42ceb8444dfde1c421f3eb16f2111208e3158ad595ea4cb411869b67e",
    "instruction_count": 18,
    "instruction_bytes": 72,
    "body_bytes": 72,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00418828](../00418/00418828.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 395 bytes

~~~c

void FUN_00acd2cc(float param_1,float param_2,undefined8 param_3,undefined4 param_4)

{
  long *plVar1;
  
  plVar1 = (long *)FUN_0081f580();
                    /* WARNING: Could not recover jumptable at 0x00acd310. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar1 + 0x40))(plVar1,0,(int)param_1,(int)param_2,param_4);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acd2cc"></a> `00acd2cc` | `e9 23 bd 6d` | stp d9,d8,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00acd2d0"></a> `00acd2d0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acd2d4"></a> `00acd2d4` | `f3 13 00 f9` | str x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acd2d8"></a> `00acd2d8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00acd2dc"></a> `00acd2dc` | `28 40 20 1e` | fmov s8,s1 | `FALL_THROUGH`
<a id="insn-00acd2e0"></a> `00acd2e0` | `09 40 20 1e` | fmov s9,s0 | `FALL_THROUGH`
<a id="insn-00acd2e4"></a> `00acd2e4` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00acd2e8"></a> `00acd2e8` | `a6 48 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acd2ec"></a> `00acd2ec` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acd2f0"></a> `00acd2f0` | `22 01 38 1e` | fcvtzs w2,s9 | `FALL_THROUGH`
<a id="insn-00acd2f4"></a> `00acd2f4` | `03 01 38 1e` | fcvtzs w3,s8 | `FALL_THROUGH`
<a id="insn-00acd2f8"></a> `00acd2f8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00acd2fc"></a> `00acd2fc` | `e4 03 13 2a` | mov w4,w19 | `FALL_THROUGH`
<a id="insn-00acd300"></a> `00acd300` | `05 21 40 f9` | ldr x5,[x8, #0x40] | `FALL_THROUGH`
<a id="insn-00acd304"></a> `00acd304` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acd308"></a> `00acd308` | `f3 13 40 f9` | ldr x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acd30c"></a> `00acd30c` | `e9 23 c3 6c` | ldp d9,d8,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00acd310"></a> `00acd310` | `a0 00 1f d6` | br x5 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00acd2cc`](#insn-00acd2cc) 範囲 `[['00acd2cc', '00acd313']]`

## 命令位置別の参照

- [`00acd2cc`](#insn-00acd2cc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd2d0`](#insn-00acd2d0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd2d4`](#insn-00acd2d4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd2e8`](#insn-00acd2e8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acd304`](#insn-00acd304) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd308`](#insn-00acd308) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acd2cc`](#insn-00acd2cc)

~~~json
{
  "source": "00acd2cc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd2d0`](#insn-00acd2d0)

~~~json
{
  "source": "00acd2d0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd2d4`](#insn-00acd2d4)

~~~json
{
  "source": "00acd2d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd2e8`](#insn-00acd2e8)

~~~json
{
  "source": "00acd2e8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd304`](#insn-00acd304)

~~~json
{
  "source": "00acd304",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd308`](#insn-00acd308)

~~~json
{
  "source": "00acd308",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
