# 004fbbdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `004d8d44`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8d44.md) · 移動量 `+0x22e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0010.md#compare-32c5907e0921686119d181446036183b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `004fbc1c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbc1c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0010.md#compare-0908535440588d15444709bdce91d972)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004fbbdc",
  "name": "_ZN5Botan11Invalid_OIDC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 204,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ff739d39043a65ba153c11ecbd22286d7aca63f9bc64670138fe923671df9c3d",
  "source_text_sha256": "ff739d39043a65ba153c11ecbd22286d7aca63f9bc64670138fe923671df9c3d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004fbbdc",
        "004fbca3"
      ],
      [
        "004fbce8",
        "004fbceb"
      ]
    ],
    "bytes_sha256": "b94315e98874aa17a44236d9808834f3a958da1193cb04c4a954e691d7319be6",
    "instruction_count": 51,
    "instruction_bytes": 204,
    "body_bytes": 204,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c583e0](../00c58/00c583e0.md)

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57cb0](../00c57/00c57cb0.md)
- [00c58380](../00c58/00c58380.md)

## 関連文字列（未確認候補）

~~~text
"Decoding error: "
"Invalid ASN.1 OID: "
"Invalid argument"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1222 bytes

~~~c

void _ZN5Botan11Invalid_OIDC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
               (long *param_1)

{
  long lVar1;
  byte local_58 [16];
  void *local_48;
  byte local_40 [16];
  void *local_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
            (local_58,"Invalid ASN.1 OID: ");
  _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
            (local_40,"Decoding error: ",local_58);
  _ZN5Botan9ExceptionC1EPKcRKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE
            (param_1,"Invalid argument",local_40);
  *param_1 = (long)(PTR__ZTVN5Botan16Invalid_ArgumentE_00c9a960 + 0x10);
  if ((local_40[0] & 1) != 0) {
    _ZdlPv(local_30);
  }
  *param_1 = (long)(PTR__ZTVN5Botan14Decoding_ErrorE_00c9a968 + 0x10);
  if ((local_58[0] & 1) != 0) {
    _ZdlPv(local_48);
  }
  *param_1 = (long)(PTR__ZTVN5Botan11Invalid_OIDE_00c9aca0 + 0x10);
  if (*(long *)(lVar1 + 0x28) == local_28) {
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
<a id="insn-004fbbdc"></a> `004fbbdc` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-004fbbe0"></a> `004fbbe0` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fbbe4"></a> `004fbbe4` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004fbbe8"></a> `004fbbe8` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-004fbbec"></a> `004fbbec` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004fbbf0"></a> `004fbbf0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004fbbf4"></a> `004fbbf4` | `e0 ed ff f0` | adrp x0,0x2ba000 | `FALL_THROUGH`
<a id="insn-004fbbf8"></a> `004fbbf8` | `00 d4 0a 91` | add x0,x0,#0x2b5 | `FALL_THROUGH`
<a id="insn-004fbbfc"></a> `004fbbfc` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-004fbc00"></a> `004fbc00` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004fbc04"></a> `004fbc04` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-004fbc08"></a> `004fbc08` | `2a 70 1d 94` | bl 0x00c57cb0 | `UNCONDITIONAL_CALL`
<a id="insn-004fbc0c"></a> `004fbc0c` | `20 ee ff 90` | adrp x0,0x2bf000 | `FALL_THROUGH`
<a id="insn-004fbc10"></a> `004fbc10` | `00 90 37 91` | add x0,x0,#0xde4 | `FALL_THROUGH`
<a id="insn-004fbc14"></a> `004fbc14` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004fbc18"></a> `004fbc18` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-004fbc1c"></a> `004fbc1c` | `25 70 1d 94` | bl 0x00c57cb0 | `UNCONDITIONAL_CALL`
<a id="insn-004fbc20"></a> `004fbc20` | `41 ed ff f0` | adrp x1,0x2a6000 | `FALL_THROUGH`
<a id="insn-004fbc24"></a> `004fbc24` | `21 c8 0d 91` | add x1,x1,#0x372 | `FALL_THROUGH`
<a id="insn-004fbc28"></a> `004fbc28` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004fbc2c"></a> `004fbc2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004fbc30"></a> `004fbc30` | `d4 71 1d 94` | bl 0x00c58380 | `UNCONDITIONAL_CALL`
<a id="insn-004fbc34"></a> `004fbc34` | `e8 3c 00 f0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-004fbc38"></a> `004fbc38` | `08 b1 44 f9` | ldr x8,[x8, #0x960] | `FALL_THROUGH`
<a id="insn-004fbc3c"></a> `004fbc3c` | `e9 83 40 39` | ldrb w9,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004fbc40"></a> `004fbc40` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004fbc44"></a> `004fbc44` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-004fbc48"></a> `004fbc48` | `69 00 00 36` | tbz w9,#0x0,0x004fbc54 | `CONDITIONAL_JUMP`
<a id="insn-004fbc4c"></a> `004fbc4c` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004fbc50"></a> `004fbc50` | `98 6f 1d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-004fbc54"></a> `004fbc54` | `e8 3c 00 f0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-004fbc58"></a> `004fbc58` | `08 b5 44 f9` | ldr x8,[x8, #0x968] | `FALL_THROUGH`
<a id="insn-004fbc5c"></a> `004fbc5c` | `e9 23 40 39` | ldrb w9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004fbc60"></a> `004fbc60` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004fbc64"></a> `004fbc64` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-004fbc68"></a> `004fbc68` | `69 00 00 36` | tbz w9,#0x0,0x004fbc74 | `CONDITIONAL_JUMP`
<a id="insn-004fbc6c"></a> `004fbc6c` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004fbc70"></a> `004fbc70` | `90 6f 1d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-004fbc74"></a> `004fbc74` | `e8 3c 00 f0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-004fbc78"></a> `004fbc78` | `08 51 46 f9` | ldr x8,[x8, #0xca0] | `FALL_THROUGH`
<a id="insn-004fbc7c"></a> `004fbc7c` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004fbc80"></a> `004fbc80` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-004fbc84"></a> `004fbc84` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-004fbc88"></a> `004fbc88` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004fbc8c"></a> `004fbc8c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004fbc90"></a> `004fbc90` | `c1 02 00 54` | b.ne 0x004fbce8 | `CONDITIONAL_JUMP`
<a id="insn-004fbc94"></a> `004fbc94` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004fbc98"></a> `004fbc98` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fbc9c"></a> `004fbc9c` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-004fbca0"></a> `004fbca0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004fbce8"></a> `004fbce8` | `7e 6f 1d 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004fbbdc`](#insn-004fbbdc) 範囲 `[['004fbbdc', '004fbc4b']]`
  - `CONDITIONAL_JUMP` [`004fbc48`](#insn-004fbc48) → [`004fbc54`](#insn-004fbc54)
  - `FALL_THROUGH` [`004fbc48`](#insn-004fbc48) → [`004fbc4c`](#insn-004fbc4c)
- ブロック [`004fbc4c`](#insn-004fbc4c) 範囲 `[['004fbc4c', '004fbc53']]`
  - `FALL_THROUGH` [`004fbc50`](#insn-004fbc50) → [`004fbc54`](#insn-004fbc54)
- ブロック [`004fbc54`](#insn-004fbc54) 範囲 `[['004fbc54', '004fbc6b']]`
  - `CONDITIONAL_JUMP` [`004fbc68`](#insn-004fbc68) → [`004fbc74`](#insn-004fbc74)
  - `FALL_THROUGH` [`004fbc68`](#insn-004fbc68) → [`004fbc6c`](#insn-004fbc6c)
- ブロック [`004fbc6c`](#insn-004fbc6c) 範囲 `[['004fbc6c', '004fbc73']]`
  - `FALL_THROUGH` [`004fbc70`](#insn-004fbc70) → [`004fbc74`](#insn-004fbc74)
- ブロック [`004fbc74`](#insn-004fbc74) 範囲 `[['004fbc74', '004fbc93']]`
  - `CONDITIONAL_JUMP` [`004fbc90`](#insn-004fbc90) → [`004fbce8`](#insn-004fbce8)
  - `FALL_THROUGH` [`004fbc90`](#insn-004fbc90) → [`004fbc94`](#insn-004fbc94)
- ブロック [`004fbc94`](#insn-004fbc94) 範囲 `[['004fbc94', '004fbca3']]`
- ブロック [`004fbce8`](#insn-004fbce8) 範囲 `[['004fbce8', '004fbceb']]`

## 命令位置別の参照

- [`004fbbe0`](#insn-004fbbe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbbe4`](#insn-004fbbe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbbf8`](#insn-004fbbf8) → `002ba2b5`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004fbc00`](#insn-004fbc00) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbc08`](#insn-004fbc08) → [`00c57cb0`](../00c57/00c57cb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57cb0` · 推定シンボル `None` · 推定型 `None`
- [`004fbc10`](#insn-004fbc10) → `002bfde4`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004fbc1c`](#insn-004fbc1c) → [`00c57cb0`](../00c57/00c57cb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57cb0` · 推定シンボル `None` · 推定型 `None`
- [`004fbc24`](#insn-004fbc24) → `002a6372`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004fbc30`](#insn-004fbc30) → [`00c58380`](../00c58/00c58380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58380` · 推定シンボル `None` · 推定型 `None`
- [`004fbc38`](#insn-004fbc38) → `00c9a960`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fbc3c`](#insn-004fbc3c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbc44`](#insn-004fbc44) → `00c67050`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`004fbc48`](#insn-004fbc48) → [`004fbc54`](#insn-004fbc54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbc4c`](#insn-004fbc4c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbc50`](#insn-004fbc50) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`004fbc58`](#insn-004fbc58) → `00c9a968`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fbc5c`](#insn-004fbc5c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbc64`](#insn-004fbc64) → `00c67258`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`004fbc68`](#insn-004fbc68) → [`004fbc74`](#insn-004fbc74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbc6c`](#insn-004fbc6c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbc70`](#insn-004fbc70) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`004fbc78`](#insn-004fbc78) → `00c9aca0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fbc80`](#insn-004fbc80) → `00c672a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`004fbc88`](#insn-004fbc88) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbc90`](#insn-004fbc90) → [`004fbce8`](#insn-004fbce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbc94`](#insn-004fbc94) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbc98`](#insn-004fbc98) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fbce8`](#insn-004fbce8) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004fbbe0`](#insn-004fbbe0)

~~~json
{
  "source": "004fbbe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbbe4`](#insn-004fbbe4)

~~~json
{
  "source": "004fbbe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbbf8`](#insn-004fbbf8)

~~~json
{
  "source": "004fbbf8",
  "target": "002ba2b5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ba2b5",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "496e76616c69642041534e2e31204f49443a2000",
  "capture_start": "002ba2b5",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004fbc00`](#insn-004fbc00)

~~~json
{
  "source": "004fbc00",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbc08`](#insn-004fbc08)

~~~json
{
  "source": "004fbc08",
  "target": "00c57cb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fbc10`](#insn-004fbc10)

~~~json
{
  "source": "004fbc10",
  "target": "002bfde4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bfde4",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "4465636f64696e67206572726f723a2000",
  "capture_start": "002bfde4",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004fbc1c`](#insn-004fbc1c)

~~~json
{
  "source": "004fbc1c",
  "target": "00c57cb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fbc24`](#insn-004fbc24)

~~~json
{
  "source": "004fbc24",
  "target": "002a6372",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a6372",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "496e76616c696420617267756d656e7400",
  "capture_start": "002a6372",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004fbc30`](#insn-004fbc30)

~~~json
{
  "source": "004fbc30",
  "target": "00c58380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fbc38`](#insn-004fbc38)

~~~json
{
  "source": "004fbc38",
  "target": "00c9a960",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a960",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fbc3c`](#insn-004fbc3c)

~~~json
{
  "source": "004fbc3c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbc44`](#insn-004fbc44)

~~~json
{
  "source": "004fbc44",
  "target": "00c67050",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67040",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004fbc48`](#insn-004fbc48)

~~~json
{
  "source": "004fbc48",
  "target": "004fbc54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbc4c`](#insn-004fbc4c)

~~~json
{
  "source": "004fbc4c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbc50`](#insn-004fbc50)

~~~json
{
  "source": "004fbc50",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fbc58`](#insn-004fbc58)

~~~json
{
  "source": "004fbc58",
  "target": "00c9a968",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a968",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fbc5c`](#insn-004fbc5c)

~~~json
{
  "source": "004fbc5c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbc64`](#insn-004fbc64)

~~~json
{
  "source": "004fbc64",
  "target": "00c67258",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67248",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004fbc68`](#insn-004fbc68)

~~~json
{
  "source": "004fbc68",
  "target": "004fbc74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbc6c`](#insn-004fbc6c)

~~~json
{
  "source": "004fbc6c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbc70`](#insn-004fbc70)

~~~json
{
  "source": "004fbc70",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fbc78`](#insn-004fbc78)

~~~json
{
  "source": "004fbc78",
  "target": "00c9aca0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9aca0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fbc80`](#insn-004fbc80)

~~~json
{
  "source": "004fbc80",
  "target": "00c672a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67298",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004fbc88`](#insn-004fbc88)

~~~json
{
  "source": "004fbc88",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbc90`](#insn-004fbc90)

~~~json
{
  "source": "004fbc90",
  "target": "004fbce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbc94`](#insn-004fbc94)

~~~json
{
  "source": "004fbc94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbc98`](#insn-004fbc98)

~~~json
{
  "source": "004fbc98",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fbce8`](#insn-004fbce8)

~~~json
{
  "source": "004fbce8",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
