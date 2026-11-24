# 00bf9fbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bf9b94`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9b94.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0040.md#compare-7c597bd207b13c31695014b925c9a73a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfa058`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa058.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-476512cc8ae28dbc012005cd71c6bd81)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf9fbc",
  "name": "_ZNSt6__ndk113shared_futureIvED1Ev",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1286c3c0a28d9d4a378feeb86b3a3cec3a05ace460e31f1e0d0039ecb60a3e4c",
  "source_text_sha256": "1286c3c0a28d9d4a378feeb86b3a3cec3a05ace460e31f1e0d0039ecb60a3e4c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf9fbc",
        "00bfa00f"
      ]
    ],
    "bytes_sha256": "aeb1f20e8d5550f4d3b936cd67b6987c68778856f704939b70104a45db733da6",
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

- [00c53d00](../00c53/00c53d00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 465 bytes

~~~c

void _ZNSt6__ndk113shared_futureIvED1Ev(undefined8 *param_1)

{
  long lVar1;
  long *plVar2;
  
  plVar2 = (long *)*param_1;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c53d00(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
                    /* WARNING: Could not recover jumptable at 0x00bfa00c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*plVar2 + 0x10))(plVar2);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf9fbc"></a> `00bf9fbc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf9fc0"></a> `00bf9fc0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bf9fc4"></a> `00bf9fc4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf9fc8"></a> `00bf9fc8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bf9fcc"></a> `00bf9fcc` | `13 00 40 f9` | ldr x19,[x0] | `FALL_THROUGH`
<a id="insn-00bf9fd0"></a> `00bf9fd0` | `b3 00 00 b4` | cbz x19,0x00bf9fe4 | `CONDITIONAL_JUMP`
<a id="insn-00bf9fd4"></a> `00bf9fd4` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00bf9fd8"></a> `00bf9fd8` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00bf9fdc"></a> `00bf9fdc` | `49 67 01 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00bf9fe0"></a> `00bf9fe0` | `a0 00 00 b4` | cbz x0,0x00bf9ff4 | `CONDITIONAL_JUMP`
<a id="insn-00bf9fe4"></a> `00bf9fe4` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf9fe8"></a> `00bf9fe8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bf9fec"></a> `00bf9fec` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf9ff0"></a> `00bf9ff0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bf9ff4"></a> `00bf9ff4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bf9ff8"></a> `00bf9ff8` | `10 09 40 f9` | ldr x16,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bf9ffc"></a> `00bf9ffc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfa000"></a> `00bfa000` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfa004"></a> `00bfa004` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfa008"></a> `00bfa008` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfa00c"></a> `00bfa00c` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bf9fbc`](#insn-00bf9fbc) 範囲 `[['00bf9fbc', '00bf9fd3']]`
  - `CONDITIONAL_JUMP` [`00bf9fd0`](#insn-00bf9fd0) → [`00bf9fe4`](#insn-00bf9fe4)
  - `FALL_THROUGH` [`00bf9fd0`](#insn-00bf9fd0) → [`00bf9fd4`](#insn-00bf9fd4)
- ブロック [`00bf9fd4`](#insn-00bf9fd4) 範囲 `[['00bf9fd4', '00bf9fe3']]`
  - `CONDITIONAL_JUMP` [`00bf9fe0`](#insn-00bf9fe0) → [`00bf9ff4`](#insn-00bf9ff4)
  - `FALL_THROUGH` [`00bf9fe0`](#insn-00bf9fe0) → [`00bf9fe4`](#insn-00bf9fe4)
- ブロック [`00bf9fe4`](#insn-00bf9fe4) 範囲 `[['00bf9fe4', '00bf9ff3']]`
- ブロック [`00bf9ff4`](#insn-00bf9ff4) 範囲 `[['00bf9ff4', '00bfa00f']]`

## 命令位置別の参照

- [`00bf9fc0`](#insn-00bf9fc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9fc4`](#insn-00bf9fc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9fd0`](#insn-00bf9fd0) → [`00bf9fe4`](#insn-00bf9fe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9fdc`](#insn-00bf9fdc) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00bf9fe0`](#insn-00bf9fe0) → [`00bf9ff4`](#insn-00bf9ff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9fe4`](#insn-00bf9fe4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9fe8`](#insn-00bf9fe8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa000`](#insn-00bfa000) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa004`](#insn-00bfa004) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf9fc0`](#insn-00bf9fc0)

~~~json
{
  "source": "00bf9fc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9fc4`](#insn-00bf9fc4)

~~~json
{
  "source": "00bf9fc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9fd0`](#insn-00bf9fd0)

~~~json
{
  "source": "00bf9fd0",
  "target": "00bf9fe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9fdc`](#insn-00bf9fdc)

~~~json
{
  "source": "00bf9fdc",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf9fe0`](#insn-00bf9fe0)

~~~json
{
  "source": "00bf9fe0",
  "target": "00bf9ff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9fe4`](#insn-00bf9fe4)

~~~json
{
  "source": "00bf9fe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9fe8`](#insn-00bf9fe8)

~~~json
{
  "source": "00bf9fe8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa000`](#insn-00bfa000)

~~~json
{
  "source": "00bfa000",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa004`](#insn-00bfa004)

~~~json
{
  "source": "00bfa004",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
