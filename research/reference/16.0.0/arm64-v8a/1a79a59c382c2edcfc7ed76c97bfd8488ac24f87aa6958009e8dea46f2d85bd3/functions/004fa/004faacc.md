# 004faacc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `004d7c34`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7c34.md) · 移動量 `+0x22e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0010.md#compare-1aa902b5ff68ddc2dcb2e7f72a305df6)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `004fab0c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fab0c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0010.md#compare-e034a4c70a4d586d553d4edecf5d8fda)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004faacc",
  "name": "_ZN5Botan14Internal_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5f46971b6d7c6bbd9ae156e88ed53affddcefbeb74ad5ad10c01f8fe0a2d05f0",
  "source_text_sha256": "5f46971b6d7c6bbd9ae156e88ed53affddcefbeb74ad5ad10c01f8fe0a2d05f0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004faacc",
        "004fab7b"
      ],
      [
        "004fabb0",
        "004fabb3"
      ]
    ],
    "bytes_sha256": "90e17f2c7fd97c737defa0339dedeec4384e3132ce8a6dc970eb17b3865e8e76",
    "instruction_count": 45,
    "instruction_bytes": 180,
    "body_bytes": 180,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c58700](../00c58/00c58700.md)
- [00c59420](../00c59/00c59420.md)

## 呼び出し先

- [0043bae0](../0043b/0043bae0.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57cb0](../00c57/00c57cb0.md)

## 関連文字列（未確認候補）

~~~text
"Internal error: "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 997 bytes

~~~c

void _ZN5Botan14Internal_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
               (long *param_1)

{
  long lVar1;
  byte local_50;
  undefined7 uStack_4f;
  long lStack_48;
  void *local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
            (&local_50,"Internal error: ");
  *param_1 = (long)(PTR__ZTVN5Botan9ExceptionE_00c9a9d0 + 0x10);
  if ((local_50 & 1) == 0) {
    param_1[2] = lStack_48;
    param_1[1] = CONCAT71(uStack_4f,local_50);
    param_1[3] = (long)local_40;
  }
  else {
    FUN_0043bae0(param_1 + 1,local_40,lStack_48);
    if ((local_50 & 1) != 0) {
      _ZdlPv(local_40);
    }
  }
  *param_1 = (long)(PTR__ZTVN5Botan14Internal_ErrorE_00c9ac40 + 0x10);
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004faacc"></a> `004faacc` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004faad0"></a> `004faad0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004faad4"></a> `004faad4` | `f5 1b 00 f9` | str x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004faad8"></a> `004faad8` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004faadc"></a> `004faadc` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004faae0"></a> `004faae0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004faae4"></a> `004faae4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004faae8"></a> `004faae8` | `a0 ed ff d0` | adrp x0,0x2b0000 | `FALL_THROUGH`
<a id="insn-004faaec"></a> `004faaec` | `00 c8 2f 91` | add x0,x0,#0xbf2 | `FALL_THROUGH`
<a id="insn-004faaf0"></a> `004faaf0` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-004faaf4"></a> `004faaf4` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004faaf8"></a> `004faaf8` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-004faafc"></a> `004faafc` | `6d 74 1d 94` | bl 0x00c57cb0 | `UNCONDITIONAL_CALL`
<a id="insn-004fab00"></a> `004fab00` | `08 3d 00 90` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-004fab04"></a> `004fab04` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004fab08"></a> `004fab08` | `08 e9 44 f9` | ldr x8,[x8, #0x9d0] | `FALL_THROUGH`
<a id="insn-004fab0c"></a> `004fab0c` | `e9 03 40 39` | ldrb w9,[sp] | `FALL_THROUGH`
<a id="insn-004fab10"></a> `004fab10` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004fab14"></a> `004fab14` | `08 84 00 f8` | str x8,[x0], #0x8 | `FALL_THROUGH`
<a id="insn-004fab18"></a> `004fab18` | `c9 00 00 37` | tbnz w9,#0x0,0x004fab30 | `CONDITIONAL_JUMP`
<a id="insn-004fab1c"></a> `004fab1c` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-004fab20"></a> `004fab20` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004fab24"></a> `004fab24` | `00 00 80 3d` | str q0,[x0] | `FALL_THROUGH`
<a id="insn-004fab28"></a> `004fab28` | `08 08 00 f9` | str x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004fab2c"></a> `004fab2c` | `07 00 00 14` | b 0x004fab48 | `UNCONDITIONAL_JUMP`
<a id="insn-004fab30"></a> `004fab30` | `e2 87 40 a9` | ldp x2,x1,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004fab34"></a> `004fab34` | `eb 03 fd 97` | bl 0x0043bae0 | `UNCONDITIONAL_CALL`
<a id="insn-004fab38"></a> `004fab38` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-004fab3c"></a> `004fab3c` | `68 00 00 36` | tbz w8,#0x0,0x004fab48 | `CONDITIONAL_JUMP`
<a id="insn-004fab40"></a> `004fab40` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004fab44"></a> `004fab44` | `db 73 1d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-004fab48"></a> `004fab48` | `08 3d 00 90` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-004fab4c"></a> `004fab4c` | `08 21 46 f9` | ldr x8,[x8, #0xc40] | `FALL_THROUGH`
<a id="insn-004fab50"></a> `004fab50` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004fab54"></a> `004fab54` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-004fab58"></a> `004fab58` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-004fab5c"></a> `004fab5c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004fab60"></a> `004fab60` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004fab64"></a> `004fab64` | `61 02 00 54` | b.ne 0x004fabb0 | `CONDITIONAL_JUMP`
<a id="insn-004fab68"></a> `004fab68` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fab6c"></a> `004fab6c` | `f5 1b 40 f9` | ldr x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004fab70"></a> `004fab70` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004fab74"></a> `004fab74` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004fab78"></a> `004fab78` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004fabb0"></a> `004fabb0` | `cc 73 1d 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004faacc`](#insn-004faacc) 範囲 `[['004faacc', '004fab1b']]`
  - `CONDITIONAL_JUMP` [`004fab18`](#insn-004fab18) → [`004fab30`](#insn-004fab30)
  - `FALL_THROUGH` [`004fab18`](#insn-004fab18) → [`004fab1c`](#insn-004fab1c)
- ブロック [`004fab1c`](#insn-004fab1c) 範囲 `[['004fab1c', '004fab2f']]`
  - `UNCONDITIONAL_JUMP` [`004fab2c`](#insn-004fab2c) → [`004fab48`](#insn-004fab48)
- ブロック [`004fab30`](#insn-004fab30) 範囲 `[['004fab30', '004fab3f']]`
  - `CONDITIONAL_JUMP` [`004fab3c`](#insn-004fab3c) → [`004fab48`](#insn-004fab48)
  - `FALL_THROUGH` [`004fab3c`](#insn-004fab3c) → [`004fab40`](#insn-004fab40)
- ブロック [`004fab40`](#insn-004fab40) 範囲 `[['004fab40', '004fab47']]`
  - `FALL_THROUGH` [`004fab44`](#insn-004fab44) → [`004fab48`](#insn-004fab48)
- ブロック [`004fab48`](#insn-004fab48) 範囲 `[['004fab48', '004fab67']]`
  - `CONDITIONAL_JUMP` [`004fab64`](#insn-004fab64) → [`004fabb0`](#insn-004fabb0)
  - `FALL_THROUGH` [`004fab64`](#insn-004fab64) → [`004fab68`](#insn-004fab68)
- ブロック [`004fab68`](#insn-004fab68) 範囲 `[['004fab68', '004fab7b']]`
- ブロック [`004fabb0`](#insn-004fabb0) 範囲 `[['004fabb0', '004fabb3']]`

## 命令位置別の参照

- [`004faad0`](#insn-004faad0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004faad4`](#insn-004faad4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004faad8`](#insn-004faad8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004faaec`](#insn-004faaec) → `002b0bf2`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004faaf4`](#insn-004faaf4) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004faafc`](#insn-004faafc) → [`00c57cb0`](../00c57/00c57cb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57cb0` · 推定シンボル `None` · 推定型 `None`
- [`004fab08`](#insn-004fab08) → `00c9a9d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fab0c`](#insn-004fab0c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fab14`](#insn-004fab14) → `00c67028`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`004fab18`](#insn-004fab18) → [`004fab30`](#insn-004fab30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fab1c`](#insn-004fab1c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fab20`](#insn-004fab20) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fab2c`](#insn-004fab2c) → [`004fab48`](#insn-004fab48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fab30`](#insn-004fab30) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fab34`](#insn-004fab34) → [`0043bae0`](../0043b/0043bae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bae0` · 推定シンボル `None` · 推定型 `None`
- [`004fab38`](#insn-004fab38) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fab3c`](#insn-004fab3c) → [`004fab48`](#insn-004fab48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fab40`](#insn-004fab40) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fab44`](#insn-004fab44) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`004fab4c`](#insn-004fab4c) → `00c9ac40`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fab54`](#insn-004fab54) → `00c670a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`004fab5c`](#insn-004fab5c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fab64`](#insn-004fab64) → [`004fabb0`](#insn-004fabb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fab68`](#insn-004fab68) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fab6c`](#insn-004fab6c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fab70`](#insn-004fab70) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fabb0`](#insn-004fabb0) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004faad0`](#insn-004faad0)

~~~json
{
  "source": "004faad0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004faad4`](#insn-004faad4)

~~~json
{
  "source": "004faad4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004faad8`](#insn-004faad8)

~~~json
{
  "source": "004faad8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004faaec`](#insn-004faaec)

~~~json
{
  "source": "004faaec",
  "target": "002b0bf2",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b0bf2",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "496e7465726e616c206572726f723a2000",
  "capture_start": "002b0bf2",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004faaf4`](#insn-004faaf4)

~~~json
{
  "source": "004faaf4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004faafc`](#insn-004faafc)

~~~json
{
  "source": "004faafc",
  "target": "00c57cb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fab08`](#insn-004fab08)

~~~json
{
  "source": "004fab08",
  "target": "00c9a9d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a9d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fab0c`](#insn-004fab0c)

~~~json
{
  "source": "004fab0c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fab14`](#insn-004fab14)

~~~json
{
  "source": "004fab14",
  "target": "00c67028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67018",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004fab18`](#insn-004fab18)

~~~json
{
  "source": "004fab18",
  "target": "004fab30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fab1c`](#insn-004fab1c)

~~~json
{
  "source": "004fab1c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fab20`](#insn-004fab20)

~~~json
{
  "source": "004fab20",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fab2c`](#insn-004fab2c)

~~~json
{
  "source": "004fab2c",
  "target": "004fab48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fab30`](#insn-004fab30)

~~~json
{
  "source": "004fab30",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fab34`](#insn-004fab34)

~~~json
{
  "source": "004fab34",
  "target": "0043bae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fab38`](#insn-004fab38)

~~~json
{
  "source": "004fab38",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fab3c`](#insn-004fab3c)

~~~json
{
  "source": "004fab3c",
  "target": "004fab48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fab40`](#insn-004fab40)

~~~json
{
  "source": "004fab40",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fab44`](#insn-004fab44)

~~~json
{
  "source": "004fab44",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fab4c`](#insn-004fab4c)

~~~json
{
  "source": "004fab4c",
  "target": "00c9ac40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ac40",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fab54`](#insn-004fab54)

~~~json
{
  "source": "004fab54",
  "target": "00c670a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67090",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004fab5c`](#insn-004fab5c)

~~~json
{
  "source": "004fab5c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fab64`](#insn-004fab64)

~~~json
{
  "source": "004fab64",
  "target": "004fabb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fab68`](#insn-004fab68)

~~~json
{
  "source": "004fab68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fab6c`](#insn-004fab6c)

~~~json
{
  "source": "004fab6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fab70`](#insn-004fab70)

~~~json
{
  "source": "004fab70",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fabb0`](#insn-004fabb0)

~~~json
{
  "source": "004fabb0",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
