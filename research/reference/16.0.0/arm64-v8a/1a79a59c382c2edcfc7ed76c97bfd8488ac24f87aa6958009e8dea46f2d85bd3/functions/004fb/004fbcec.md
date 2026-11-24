# 004fbcec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `004d8e54`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8e54.md) · 移動量 `+0x22e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0010.md#compare-fb13e921795aba31ca8f8cd6a3f5999f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `004fbd2c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbd2c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0010.md#compare-d91f2dcc838a480206d0e97de31f0656)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004fbcec",
  "name": "_ZN5Botan15Stream_IO_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a53690425b88d565ba180c8f3be2191e3fca97f7a2038660ced3c381cf5d3814",
  "source_text_sha256": "a53690425b88d565ba180c8f3be2191e3fca97f7a2038660ced3c381cf5d3814",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004fbcec",
        "004fbd9b"
      ],
      [
        "004fbdd0",
        "004fbdd3"
      ]
    ],
    "bytes_sha256": "a2f29d3cbe1899ecc98a5a0cc5befc6d9b0c9210fdede4ac248247669899149d",
    "instruction_count": 45,
    "instruction_bytes": 180,
    "body_bytes": 180,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c583b0](../00c58/00c583b0.md)

## 呼び出し先

- [0043bae0](../0043b/0043bae0.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57cb0](../00c57/00c57cb0.md)

## 関連文字列（未確認候補）

~~~text
"I/O error: "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 994 bytes

~~~c

void _ZN5Botan15Stream_IO_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
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
            (&local_50,"I/O error: ");
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
  *param_1 = (long)(PTR__ZTVN5Botan15Stream_IO_ErrorE_00c9aca8 + 0x10);
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
<a id="insn-004fbcec"></a> `004fbcec` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004fbcf0"></a> `004fbcf0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004fbcf4"></a> `004fbcf4` | `f5 1b 00 f9` | str x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004fbcf8"></a> `004fbcf8` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fbcfc"></a> `004fbcfc` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004fbd00"></a> `004fbd00` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004fbd04"></a> `004fbd04` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004fbd08"></a> `004fbd08` | `c0 ed ff b0` | adrp x0,0x2b4000 | `FALL_THROUGH`
<a id="insn-004fbd0c"></a> `004fbd0c` | `00 20 37 91` | add x0,x0,#0xdc8 | `FALL_THROUGH`
<a id="insn-004fbd10"></a> `004fbd10` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-004fbd14"></a> `004fbd14` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004fbd18"></a> `004fbd18` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-004fbd1c"></a> `004fbd1c` | `e5 6f 1d 94` | bl 0x00c57cb0 | `UNCONDITIONAL_CALL`
<a id="insn-004fbd20"></a> `004fbd20` | `e8 3c 00 f0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-004fbd24"></a> `004fbd24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004fbd28"></a> `004fbd28` | `08 e9 44 f9` | ldr x8,[x8, #0x9d0] | `FALL_THROUGH`
<a id="insn-004fbd2c"></a> `004fbd2c` | `e9 03 40 39` | ldrb w9,[sp] | `FALL_THROUGH`
<a id="insn-004fbd30"></a> `004fbd30` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004fbd34"></a> `004fbd34` | `08 84 00 f8` | str x8,[x0], #0x8 | `FALL_THROUGH`
<a id="insn-004fbd38"></a> `004fbd38` | `c9 00 00 37` | tbnz w9,#0x0,0x004fbd50 | `CONDITIONAL_JUMP`
<a id="insn-004fbd3c"></a> `004fbd3c` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-004fbd40"></a> `004fbd40` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004fbd44"></a> `004fbd44` | `00 00 80 3d` | str q0,[x0] | `FALL_THROUGH`
<a id="insn-004fbd48"></a> `004fbd48` | `08 08 00 f9` | str x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004fbd4c"></a> `004fbd4c` | `07 00 00 14` | b 0x004fbd68 | `UNCONDITIONAL_JUMP`
<a id="insn-004fbd50"></a> `004fbd50` | `e2 87 40 a9` | ldp x2,x1,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004fbd54"></a> `004fbd54` | `63 ff fc 97` | bl 0x0043bae0 | `UNCONDITIONAL_CALL`
<a id="insn-004fbd58"></a> `004fbd58` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-004fbd5c"></a> `004fbd5c` | `68 00 00 36` | tbz w8,#0x0,0x004fbd68 | `CONDITIONAL_JUMP`
<a id="insn-004fbd60"></a> `004fbd60` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004fbd64"></a> `004fbd64` | `53 6f 1d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-004fbd68"></a> `004fbd68` | `e8 3c 00 f0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-004fbd6c"></a> `004fbd6c` | `08 55 46 f9` | ldr x8,[x8, #0xca8] | `FALL_THROUGH`
<a id="insn-004fbd70"></a> `004fbd70` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004fbd74"></a> `004fbd74` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-004fbd78"></a> `004fbd78` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-004fbd7c"></a> `004fbd7c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004fbd80"></a> `004fbd80` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004fbd84"></a> `004fbd84` | `61 02 00 54` | b.ne 0x004fbdd0 | `CONDITIONAL_JUMP`
<a id="insn-004fbd88"></a> `004fbd88` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fbd8c"></a> `004fbd8c` | `f5 1b 40 f9` | ldr x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004fbd90"></a> `004fbd90` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004fbd94"></a> `004fbd94` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004fbd98"></a> `004fbd98` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004fbdd0"></a> `004fbdd0` | `44 6f 1d 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004fbcec`](#insn-004fbcec) 範囲 `[['004fbcec', '004fbd3b']]`
  - `CONDITIONAL_JUMP` [`004fbd38`](#insn-004fbd38) → [`004fbd50`](#insn-004fbd50)
  - `FALL_THROUGH` [`004fbd38`](#insn-004fbd38) → [`004fbd3c`](#insn-004fbd3c)
- ブロック [`004fbd3c`](#insn-004fbd3c) 範囲 `[['004fbd3c', '004fbd4f']]`
  - `UNCONDITIONAL_JUMP` [`004fbd4c`](#insn-004fbd4c) → [`004fbd68`](#insn-004fbd68)
- ブロック [`004fbd50`](#insn-004fbd50) 範囲 `[['004fbd50', '004fbd5f']]`
  - `CONDITIONAL_JUMP` [`004fbd5c`](#insn-004fbd5c) → [`004fbd68`](#insn-004fbd68)
  - `FALL_THROUGH` [`004fbd5c`](#insn-004fbd5c) → [`004fbd60`](#insn-004fbd60)
- ブロック [`004fbd60`](#insn-004fbd60) 範囲 `[['004fbd60', '004fbd67']]`
  - `FALL_THROUGH` [`004fbd64`](#insn-004fbd64) → [`004fbd68`](#insn-004fbd68)
- ブロック [`004fbd68`](#insn-004fbd68) 範囲 `[['004fbd68', '004fbd87']]`
  - `CONDITIONAL_JUMP` [`004fbd84`](#insn-004fbd84) → [`004fbdd0`](#insn-004fbdd0)
  - `FALL_THROUGH` [`004fbd84`](#insn-004fbd84) → [`004fbd88`](#insn-004fbd88)
- ブロック [`004fbd88`](#insn-004fbd88) 範囲 `[['004fbd88', '004fbd9b']]`
- ブロック [`004fbdd0`](#insn-004fbdd0) 範囲 `[['004fbdd0', '004fbdd3']]`

## 命令位置別の参照

- [`004fbcf0`](#insn-004fbcf0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbcf4`](#insn-004fbcf4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbcf8`](#insn-004fbcf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbd0c`](#insn-004fbd0c) → `002b4dc8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004fbd14`](#insn-004fbd14) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbd1c`](#insn-004fbd1c) → [`00c57cb0`](../00c57/00c57cb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57cb0` · 推定シンボル `None` · 推定型 `None`
- [`004fbd28`](#insn-004fbd28) → `00c9a9d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fbd2c`](#insn-004fbd2c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbd34`](#insn-004fbd34) → `00c67028`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`004fbd38`](#insn-004fbd38) → [`004fbd50`](#insn-004fbd50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbd3c`](#insn-004fbd3c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbd40`](#insn-004fbd40) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbd4c`](#insn-004fbd4c) → [`004fbd68`](#insn-004fbd68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbd50`](#insn-004fbd50) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbd54`](#insn-004fbd54) → [`0043bae0`](../0043b/0043bae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bae0` · 推定シンボル `None` · 推定型 `None`
- [`004fbd58`](#insn-004fbd58) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbd5c`](#insn-004fbd5c) → [`004fbd68`](#insn-004fbd68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbd60`](#insn-004fbd60) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbd64`](#insn-004fbd64) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`004fbd6c`](#insn-004fbd6c) → `00c9aca8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fbd74`](#insn-004fbd74) → `00c672d0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`004fbd7c`](#insn-004fbd7c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbd84`](#insn-004fbd84) → [`004fbdd0`](#insn-004fbdd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbd88`](#insn-004fbd88) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbd8c`](#insn-004fbd8c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbd90`](#insn-004fbd90) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbdd0`](#insn-004fbdd0) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004fbcf0`](#insn-004fbcf0)

~~~json
{
  "source": "004fbcf0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbcf4`](#insn-004fbcf4)

~~~json
{
  "source": "004fbcf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbcf8`](#insn-004fbcf8)

~~~json
{
  "source": "004fbcf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbd0c`](#insn-004fbd0c)

~~~json
{
  "source": "004fbd0c",
  "target": "002b4dc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b4dc8",
  "offset": 0,
  "size": 12,
  "datatype": "string",
  "bytes": "492f4f206572726f723a2000",
  "capture_start": "002b4dc8",
  "capture_bytes": 12,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004fbd14`](#insn-004fbd14)

~~~json
{
  "source": "004fbd14",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbd1c`](#insn-004fbd1c)

~~~json
{
  "source": "004fbd1c",
  "target": "00c57cb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fbd28`](#insn-004fbd28)

~~~json
{
  "source": "004fbd28",
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
- 参照命令 [`004fbd2c`](#insn-004fbd2c)

~~~json
{
  "source": "004fbd2c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbd34`](#insn-004fbd34)

~~~json
{
  "source": "004fbd34",
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
- 参照命令 [`004fbd38`](#insn-004fbd38)

~~~json
{
  "source": "004fbd38",
  "target": "004fbd50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbd3c`](#insn-004fbd3c)

~~~json
{
  "source": "004fbd3c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbd40`](#insn-004fbd40)

~~~json
{
  "source": "004fbd40",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbd4c`](#insn-004fbd4c)

~~~json
{
  "source": "004fbd4c",
  "target": "004fbd68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbd50`](#insn-004fbd50)

~~~json
{
  "source": "004fbd50",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbd54`](#insn-004fbd54)

~~~json
{
  "source": "004fbd54",
  "target": "0043bae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fbd58`](#insn-004fbd58)

~~~json
{
  "source": "004fbd58",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbd5c`](#insn-004fbd5c)

~~~json
{
  "source": "004fbd5c",
  "target": "004fbd68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbd60`](#insn-004fbd60)

~~~json
{
  "source": "004fbd60",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbd64`](#insn-004fbd64)

~~~json
{
  "source": "004fbd64",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fbd6c`](#insn-004fbd6c)

~~~json
{
  "source": "004fbd6c",
  "target": "00c9aca8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9aca8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fbd74`](#insn-004fbd74)

~~~json
{
  "source": "004fbd74",
  "target": "00c672d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c672c0",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004fbd7c`](#insn-004fbd7c)

~~~json
{
  "source": "004fbd7c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbd84`](#insn-004fbd84)

~~~json
{
  "source": "004fbd84",
  "target": "004fbdd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbd88`](#insn-004fbd88)

~~~json
{
  "source": "004fbd88",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbd8c`](#insn-004fbd8c)

~~~json
{
  "source": "004fbd8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbd90`](#insn-004fbd90)

~~~json
{
  "source": "004fbd90",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbdd0`](#insn-004fbdd0)

~~~json
{
  "source": "004fbdd0",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
