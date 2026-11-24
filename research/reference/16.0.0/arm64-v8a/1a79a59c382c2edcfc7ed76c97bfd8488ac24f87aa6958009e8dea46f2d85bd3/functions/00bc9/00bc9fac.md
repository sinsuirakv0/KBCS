# 00bc9fac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5aaac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5aaac.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0019.md#compare-a27e0893772688337380b0ea426b2297)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bca3d4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca3d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0039.md#compare-267140ddb15bf358c83d583a59530783)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc9fac",
  "name": "_ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternalD1Ev",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bc11d15c30ab1c3ca3836fa5312c9aabe5b9a32fdab81ccd5e18473ab0891829",
  "source_text_sha256": "bc11d15c30ab1c3ca3836fa5312c9aabe5b9a32fdab81ccd5e18473ab0891829",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc9fac",
        "00bca023"
      ]
    ],
    "bytes_sha256": "800c62ecc397718b94614d5eb314ca36872a153e19a1ace112a2dc30fac0b91f",
    "instruction_count": 30,
    "instruction_bytes": 120,
    "body_bytes": 120,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00c5d290](../00c5d/00c5d290.md)

## 呼び出し先

- [00b60d04](../00b60/00b60d04.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1104 bytes

~~~c

void _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternalD1Ev
               (long param_1)

{
  long *plVar1;
  code *UNRECOVERED_JUMPTABLE;
  
  if (*(char *)(param_1 + 0x40) == '\0') {
    *(undefined1 *)(param_1 + 0x40) = 1;
    if (*(long **)(param_1 + 0x30) == (long *)0x0) {
                    /* WARNING: Subroutine does not return */
      FUN_00b60d04();
    }
    (**(code **)(**(long **)(param_1 + 0x30) + 0x30))();
  }
  plVar1 = *(long **)(param_1 + 0x30);
  if ((long *)(param_1 + 0x10) == plVar1) {
    UNRECOVERED_JUMPTABLE = *(code **)(*plVar1 + 0x20);
  }
  else {
                    /* catch() { ... } // from try @ 00bc9df8 with catch @ 00bc9ff0 */
    if (plVar1 == (long *)0x0) {
      return;
    }
                    /* catch() { ... } // from try @ 00bc9ef0 with catch @ 00bc9ff4 */
    UNRECOVERED_JUMPTABLE = *(code **)(*plVar1 + 0x28);
  }
                    /* WARNING: Could not recover jumptable at 0x00bca010. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (*UNRECOVERED_JUMPTABLE)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc9fac"></a> `00bc9fac` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bc9fb0"></a> `00bc9fb0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9fb4"></a> `00bc9fb4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bc9fb8"></a> `00bc9fb8` | `08 00 41 39` | ldrb w8,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00bc9fbc"></a> `00bc9fbc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bc9fc0"></a> `00bc9fc0` | `08 01 00 35` | cbnz w8,0x00bc9fe0 | `CONDITIONAL_JUMP`
<a id="insn-00bc9fc4"></a> `00bc9fc4` | `60 1a 40 f9` | ldr x0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00bc9fc8"></a> `00bc9fc8` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bc9fcc"></a> `00bc9fcc` | `68 02 01 39` | strb w8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00bc9fd0"></a> `00bc9fd0` | `80 02 00 b4` | cbz x0,0x00bca020 | `CONDITIONAL_JUMP`
<a id="insn-00bc9fd4"></a> `00bc9fd4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bc9fd8"></a> `00bc9fd8` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00bc9fdc"></a> `00bc9fdc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc9fe0"></a> `00bc9fe0` | `60 1a 40 f9` | ldr x0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00bc9fe4"></a> `00bc9fe4` | `68 42 00 91` | add x8,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00bc9fe8"></a> `00bc9fe8` | `1f 01 00 eb` | cmp x8,x0 | `FALL_THROUGH`
<a id="insn-00bc9fec"></a> `00bc9fec` | `a0 00 00 54` | b.eq 0x00bca000 | `CONDITIONAL_JUMP`
<a id="insn-00bc9ff0"></a> `00bc9ff0` | `20 01 00 b4` | cbz x0,0x00bca014 | `CONDITIONAL_JUMP`
<a id="insn-00bc9ff4"></a> `00bc9ff4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bc9ff8"></a> `00bc9ff8` | `01 15 40 f9` | ldr x1,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bc9ffc"></a> `00bc9ffc` | `03 00 00 14` | b 0x00bca008 | `UNCONDITIONAL_JUMP`
<a id="insn-00bca000"></a> `00bca000` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bca004"></a> `00bca004` | `01 11 40 f9` | ldr x1,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bca008"></a> `00bca008` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bca00c"></a> `00bca00c` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bca010"></a> `00bca010` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`
<a id="insn-00bca014"></a> `00bca014` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bca018"></a> `00bca018` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bca01c"></a> `00bca01c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bca020"></a> `00bca020` | `39 5b fe 97` | bl 0x00b60d04 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc9fac`](#insn-00bc9fac) 範囲 `[['00bc9fac', '00bc9fc3']]`
  - `CONDITIONAL_JUMP` [`00bc9fc0`](#insn-00bc9fc0) → [`00bc9fe0`](#insn-00bc9fe0)
  - `FALL_THROUGH` [`00bc9fc0`](#insn-00bc9fc0) → [`00bc9fc4`](#insn-00bc9fc4)
- ブロック [`00bc9fc4`](#insn-00bc9fc4) 範囲 `[['00bc9fc4', '00bc9fd3']]`
  - `CONDITIONAL_JUMP` [`00bc9fd0`](#insn-00bc9fd0) → [`00bca020`](#insn-00bca020)
  - `FALL_THROUGH` [`00bc9fd0`](#insn-00bc9fd0) → [`00bc9fd4`](#insn-00bc9fd4)
- ブロック [`00bc9fd4`](#insn-00bc9fd4) 範囲 `[['00bc9fd4', '00bc9fdf']]`
  - `FALL_THROUGH` [`00bc9fdc`](#insn-00bc9fdc) → [`00bc9fe0`](#insn-00bc9fe0)
- ブロック [`00bc9fe0`](#insn-00bc9fe0) 範囲 `[['00bc9fe0', '00bc9fef']]`
  - `CONDITIONAL_JUMP` [`00bc9fec`](#insn-00bc9fec) → [`00bca000`](#insn-00bca000)
  - `FALL_THROUGH` [`00bc9fec`](#insn-00bc9fec) → [`00bc9ff0`](#insn-00bc9ff0)
- ブロック [`00bc9ff0`](#insn-00bc9ff0) 範囲 `[['00bc9ff0', '00bc9ff3']]`
  - `CONDITIONAL_JUMP` [`00bc9ff0`](#insn-00bc9ff0) → [`00bca014`](#insn-00bca014)
  - `FALL_THROUGH` [`00bc9ff0`](#insn-00bc9ff0) → [`00bc9ff4`](#insn-00bc9ff4)
- ブロック [`00bc9ff4`](#insn-00bc9ff4) 範囲 `[['00bc9ff4', '00bc9fff']]`
  - `UNCONDITIONAL_JUMP` [`00bc9ffc`](#insn-00bc9ffc) → [`00bca008`](#insn-00bca008)
- ブロック [`00bca000`](#insn-00bca000) 範囲 `[['00bca000', '00bca007']]`
  - `FALL_THROUGH` [`00bca004`](#insn-00bca004) → [`00bca008`](#insn-00bca008)
- ブロック [`00bca008`](#insn-00bca008) 範囲 `[['00bca008', '00bca013']]`
- ブロック [`00bca014`](#insn-00bca014) 範囲 `[['00bca014', '00bca01f']]`
- ブロック [`00bca020`](#insn-00bca020) 範囲 `[['00bca020', '00bca023']]`

## 命令位置別の参照

- [`00bc9fac`](#insn-00bc9fac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9fb0`](#insn-00bc9fb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9fc0`](#insn-00bc9fc0) → [`00bc9fe0`](#insn-00bc9fe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9fd0`](#insn-00bc9fd0) → [`00bca020`](#insn-00bca020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9fec`](#insn-00bc9fec) → [`00bca000`](#insn-00bca000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9ff0`](#insn-00bc9ff0) → [`00bca014`](#insn-00bca014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9ffc`](#insn-00bc9ffc) → [`00bca008`](#insn-00bca008) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca008`](#insn-00bca008) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca014`](#insn-00bca014) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca020`](#insn-00bca020) → [`00b60d04`](../00b60/00b60d04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b60d04` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc9fac`](#insn-00bc9fac)

~~~json
{
  "source": "00bc9fac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9fb0`](#insn-00bc9fb0)

~~~json
{
  "source": "00bc9fb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9fc0`](#insn-00bc9fc0)

~~~json
{
  "source": "00bc9fc0",
  "target": "00bc9fe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9fd0`](#insn-00bc9fd0)

~~~json
{
  "source": "00bc9fd0",
  "target": "00bca020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9fec`](#insn-00bc9fec)

~~~json
{
  "source": "00bc9fec",
  "target": "00bca000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9ff0`](#insn-00bc9ff0)

~~~json
{
  "source": "00bc9ff0",
  "target": "00bca014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9ffc`](#insn-00bc9ffc)

~~~json
{
  "source": "00bc9ffc",
  "target": "00bca008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca008`](#insn-00bca008)

~~~json
{
  "source": "00bca008",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca014`](#insn-00bca014)

~~~json
{
  "source": "00bca014",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca020`](#insn-00bca020)

~~~json
{
  "source": "00bca020",
  "target": "00b60d04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
