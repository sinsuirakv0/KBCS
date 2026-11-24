# 00aff2cc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00afeea4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afeea4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0066.md#compare-a4d620983c1b7bba5dfb5fc2f72033b1)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aff368`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aff/00aff368.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0067.md#compare-ce9e06dcfe1c98db1f949338e2ee8c0f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aff2cc",
  "name": "FUN_00aff2cc",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1da62d81b7a74850beead82b12910edde0c3a03a3dcbdd802905d46f91fa17fd",
  "source_text_sha256": "1da62d81b7a74850beead82b12910edde0c3a03a3dcbdd802905d46f91fa17fd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aff2cc",
        "00aff39b"
      ]
    ],
    "bytes_sha256": "ebfb5cef629f549cb966ceb296196ce0759d7c649e720ac08c76f7c81d1d0717",
    "instruction_count": 52,
    "instruction_bytes": 208,
    "body_bytes": 208,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00685588](../00685/00685588.md)
- [006c52f8](../006c5/006c52f8.md)
- [00a4f3b4](../00a4f/00a4f3b4.md)
- [00af5a94](../00af5/00af5a94.md)
- [00b009dc](../00b00/00b009dc.md)

## 呼び出し先

- [005e7420](../005e7/005e7420.md)
- [008514f8](../00851/008514f8.md)
- [00b04c7c](../00b04/00b04c7c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 846 bytes

~~~c

ulong FUN_00aff2cc(int param_1,int param_2,int param_3,ulong param_4)

{
  int iVar1;
  long lVar2;
  ulong uVar3;
  
                    /* try { // try from 00aff2cc to 00bff2f7 has its CatchHandler @ 00aff258 */
                    /* catch() { ... } // from try @ 00aff2ac with catch @ 00aff2e4 */
  lVar2 = FUN_008514f8();
  uVar3 = FUN_005e7420(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  lVar2 = FUN_008514f8();
  if ((uVar3 & 1) == 0) {
    uVar3 = (ulong)(*(int *)((long)__DT_JMPREL + lVar2 + ((long)param_2 + 2) * 0x1c4 + 0x1840) != 0)
    ;
  }
  else {
    iVar1 = *(int *)(lVar2 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f724);
    uVar3 = (ulong)(iVar1 != 0);
    if ((iVar1 == 0) && ((param_4 & 1) != 0)) {
      uVar3 = FUN_00b04c7c(param_1,param_2,param_3,0x20);
      return uVar3;
    }
  }
  return uVar3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aff2cc"></a> `00aff2cc` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00aff2d0"></a> `00aff2d0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aff2d4"></a> `00aff2d4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aff2d8"></a> `00aff2d8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aff2dc"></a> `00aff2dc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aff2e0"></a> `00aff2e0` | `f6 03 03 2a` | mov w22,w3 | `FALL_THROUGH`
<a id="insn-00aff2e4"></a> `00aff2e4` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00aff2e8"></a> `00aff2e8` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00aff2ec"></a> `00aff2ec` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aff2f0"></a> `00aff2f0` | `82 48 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aff2f4"></a> `00aff2f4` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00aff2f8"></a> `00aff2f8` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00aff2fc"></a> `00aff2fc` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00aff300"></a> `00aff300` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00aff304"></a> `00aff304` | `47 a0 eb 97` | bl 0x005e7420 | `UNCONDITIONAL_CALL`
<a id="insn-00aff308"></a> `00aff308` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00aff30c"></a> `00aff30c` | `7b 48 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aff310"></a> `00aff310` | `88 7e 40 93` | sxtw x8,w20 | `FALL_THROUGH`
<a id="insn-00aff314"></a> `00aff314` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00aff318"></a> `00aff318` | `b7 01 00 37` | tbnz w23,#0x0,0x00aff34c | `CONDITIONAL_JUMP`
<a id="insn-00aff31c"></a> `00aff31c` | `89 38 80 52` | mov w9,#0x1c4 | `FALL_THROUGH`
<a id="insn-00aff320"></a> `00aff320` | `08 01 09 9b` | madd x8,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00aff324"></a> `00aff324` | `09 5b 9a 52` | mov w9,#0xd2d8 | `FALL_THROUGH`
<a id="insn-00aff328"></a> `00aff328` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00aff32c"></a> `00aff32c` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aff330"></a> `00aff330` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00aff334"></a> `00aff334` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00aff338"></a> `00aff338` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aff33c"></a> `00aff33c` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aff340"></a> `00aff340` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aff344"></a> `00aff344` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00aff348"></a> `00aff348` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aff34c"></a> `00aff34c` | `09 ee 80 52` | mov w9,#0x770 | `FALL_THROUGH`
<a id="insn-00aff350"></a> `00aff350` | `08 01 09 9b` | madd x8,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00aff354"></a> `00aff354` | `89 3b 80 52` | mov w9,#0x1dc | `FALL_THROUGH`
<a id="insn-00aff358"></a> `00aff358` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00aff35c"></a> `00aff35c` | `89 e4 9e 52` | mov w9,#0xf724 | `FALL_THROUGH`
<a id="insn-00aff360"></a> `00aff360` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00aff364"></a> `00aff364` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aff368"></a> `00aff368` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00aff36c"></a> `00aff36c` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00aff370"></a> `00aff370` | `48 fe ff 35` | cbnz w8,0x00aff338 | `CONDITIONAL_JUMP`
<a id="insn-00aff374"></a> `00aff374` | `36 fe 07 36` | tbz w22,#0x0,0x00aff338 | `CONDITIONAL_JUMP`
<a id="insn-00aff378"></a> `00aff378` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00aff37c"></a> `00aff37c` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00aff380"></a> `00aff380` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00aff384"></a> `00aff384` | `03 04 80 52` | mov w3,#0x20 | `FALL_THROUGH`
<a id="insn-00aff388"></a> `00aff388` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aff38c"></a> `00aff38c` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aff390"></a> `00aff390` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aff394"></a> `00aff394` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00aff398"></a> `00aff398` | `39 16 00 14` | b 0x00b04c7c | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aff2cc`](#insn-00aff2cc) 範囲 `[['00aff2cc', '00aff2e3']]`
  - `FALL_THROUGH` [`00aff2e0`](#insn-00aff2e0) → [`00aff2e4`](#insn-00aff2e4)
- ブロック [`00aff2e4`](#insn-00aff2e4) 範囲 `[['00aff2e4', '00aff31b']]`
  - `CONDITIONAL_JUMP` [`00aff318`](#insn-00aff318) → [`00aff34c`](#insn-00aff34c)
  - `FALL_THROUGH` [`00aff318`](#insn-00aff318) → [`00aff31c`](#insn-00aff31c)
- ブロック [`00aff31c`](#insn-00aff31c) 範囲 `[['00aff31c', '00aff337']]`
  - `FALL_THROUGH` [`00aff334`](#insn-00aff334) → [`00aff338`](#insn-00aff338)
- ブロック [`00aff338`](#insn-00aff338) 範囲 `[['00aff338', '00aff34b']]`
- ブロック [`00aff34c`](#insn-00aff34c) 範囲 `[['00aff34c', '00aff373']]`
  - `CONDITIONAL_JUMP` [`00aff370`](#insn-00aff370) → [`00aff338`](#insn-00aff338)
  - `FALL_THROUGH` [`00aff370`](#insn-00aff370) → [`00aff374`](#insn-00aff374)
- ブロック [`00aff374`](#insn-00aff374) 範囲 `[['00aff374', '00aff377']]`
  - `CONDITIONAL_JUMP` [`00aff374`](#insn-00aff374) → [`00aff338`](#insn-00aff338)
  - `FALL_THROUGH` [`00aff374`](#insn-00aff374) → [`00aff378`](#insn-00aff378)
- ブロック [`00aff378`](#insn-00aff378) 範囲 `[['00aff378', '00aff39b']]`

## 命令位置別の参照

- [`00aff2cc`](#insn-00aff2cc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff2d0`](#insn-00aff2d0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff2d4`](#insn-00aff2d4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff2d8`](#insn-00aff2d8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff2f0`](#insn-00aff2f0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00aff304`](#insn-00aff304) → [`005e7420`](../005e7/005e7420.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7420` · 推定シンボル `None` · 推定型 `None`
- [`00aff30c`](#insn-00aff30c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00aff318`](#insn-00aff318) → [`00aff34c`](#insn-00aff34c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff32c`](#insn-00aff32c) → `0023d2d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff338`](#insn-00aff338) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff33c`](#insn-00aff33c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff340`](#insn-00aff340) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff344`](#insn-00aff344) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff370`](#insn-00aff370) → [`00aff338`](#insn-00aff338) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff374`](#insn-00aff374) → [`00aff338`](#insn-00aff338) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff388`](#insn-00aff388) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff38c`](#insn-00aff38c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff390`](#insn-00aff390) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff394`](#insn-00aff394) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff398`](#insn-00aff398) → [`00b04c7c`](../00b04/00b04c7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b04c7c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aff2cc`](#insn-00aff2cc)

~~~json
{
  "source": "00aff2cc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff2d0`](#insn-00aff2d0)

~~~json
{
  "source": "00aff2d0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff2d4`](#insn-00aff2d4)

~~~json
{
  "source": "00aff2d4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff2d8`](#insn-00aff2d8)

~~~json
{
  "source": "00aff2d8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff2f0`](#insn-00aff2f0)

~~~json
{
  "source": "00aff2f0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff304`](#insn-00aff304)

~~~json
{
  "source": "00aff304",
  "target": "005e7420",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff30c`](#insn-00aff30c)

~~~json
{
  "source": "00aff30c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff318`](#insn-00aff318)

~~~json
{
  "source": "00aff318",
  "target": "00aff34c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff32c`](#insn-00aff32c)

~~~json
{
  "source": "00aff32c",
  "target": "0023d2d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6208,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff338`](#insn-00aff338)

~~~json
{
  "source": "00aff338",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff33c`](#insn-00aff33c)

~~~json
{
  "source": "00aff33c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff340`](#insn-00aff340)

~~~json
{
  "source": "00aff340",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff344`](#insn-00aff344)

~~~json
{
  "source": "00aff344",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff370`](#insn-00aff370)

~~~json
{
  "source": "00aff370",
  "target": "00aff338",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff374`](#insn-00aff374)

~~~json
{
  "source": "00aff374",
  "target": "00aff338",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff388`](#insn-00aff388)

~~~json
{
  "source": "00aff388",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff38c`](#insn-00aff38c)

~~~json
{
  "source": "00aff38c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff390`](#insn-00aff390)

~~~json
{
  "source": "00aff390",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff394`](#insn-00aff394)

~~~json
{
  "source": "00aff394",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff398`](#insn-00aff398)

~~~json
{
  "source": "00aff398",
  "target": "00b04c7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
