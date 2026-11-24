# 00b7dafc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b7d6d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d6d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0009.md#compare-c309d669ce7d94f761482477d509b16c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b7db98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7db98.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0077.md#compare-cdf76a072035d17934a8800cee38ed1f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b7dafc",
  "name": "_ZN11flatbuffers21FlatBufferBuilderImplILb0EE10AddElementIsEEvtT_",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "630dfb6656e7f902d2088276921fc3222257c96c911a8dffcd966fd042305e76",
  "source_text_sha256": "630dfb6656e7f902d2088276921fc3222257c96c911a8dffcd966fd042305e76",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b7dafc",
        "00b7dc0f"
      ]
    ],
    "bytes_sha256": "74c2967f6365ccdc38c7ec82609da0015ee1c063e848029d4b78daf7e6e81fb9",
    "instruction_count": 69,
    "instruction_bytes": 276,
    "body_bytes": 276,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5c1f0](../00c5c/00c5c1f0.md)

## 呼び出し先

- [00c5c1a0](../00c5c/00c5c1a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1915 bytes

~~~c

void _ZN11flatbuffers21FlatBufferBuilderImplILb0EE10AddElementIsEEvtT_
               (long param_1,uint param_2,undefined2 param_3)

{
  int iVar1;
  uint uVar2;
  ulong *puVar3;
  long lVar4;
  ulong uVar5;
  
                    /* catch() { ... } // from try @ 00b7d28c with catch @ 00b7db0c */
                    /* catch() { ... } // from try @ 00b7d2bc with catch @ 00b7db14 */
  if (*(ulong *)(param_1 + 0x68) < 2) {
    *(undefined8 *)(param_1 + 0x68) = 2;
  }
  uVar2 = *(uint *)(param_1 + 0x30);
  uVar5 = (ulong)uVar2 & 1;
  if ((int)uVar5 != 0) {
    lVar4 = *(long *)(param_1 + 0x40);
    if ((uint)((int)lVar4 - *(int *)(param_1 + 0x48)) < uVar5) {
      _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,uVar5);
      lVar4 = *(long *)(param_1 + 0x40);
      uVar2 = *(uint *)(param_1 + 0x30);
    }
    *(undefined1 **)(param_1 + 0x40) = (undefined1 *)(lVar4 - uVar5);
    *(uint *)(param_1 + 0x30) = uVar2 + (int)uVar5;
    *(undefined1 *)(lVar4 - uVar5) = 0;
  }
  lVar4 = *(long *)(param_1 + 0x40);
  puVar3 = *(ulong **)(param_1 + 0x48);
  if (((int)lVar4 - (int)puVar3 & 0xfffffffeU) == 0) {
    _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,2);
    lVar4 = *(long *)(param_1 + 0x40);
    puVar3 = *(ulong **)(param_1 + 0x48);
  }
  *(long *)(param_1 + 0x40) = lVar4 + -2;
  iVar1 = *(int *)(param_1 + 0x30) + 2;
  *(int *)(param_1 + 0x30) = iVar1;
  *(undefined2 *)(lVar4 + -2) = param_3;
  if (((int)(lVar4 + -2) - (int)puVar3 & 0xfffffff8U) == 0) {
    _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,8);
    puVar3 = *(ulong **)(param_1 + 0x48);
  }
  *puVar3 = CONCAT44(param_2,iVar1) & 0xffffffffffff;
  *(long *)(param_1 + 0x48) = *(long *)(param_1 + 0x48) + 8;
  *(int *)(param_1 + 0x50) = *(int *)(param_1 + 0x50) + 1;
  if ((uint)*(ushort *)(param_1 + 0x54) < (param_2 & 0xffff)) {
    *(short *)(param_1 + 0x54) = (short)param_2;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b7dafc"></a> `00b7dafc` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b7db00"></a> `00b7db00` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7db04"></a> `00b7db04` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b7db08"></a> `00b7db08` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b7db0c"></a> `00b7db0c` | `08 34 40 f9` | ldr x8,[x0, #0x68] | `FALL_THROUGH`
<a id="insn-00b7db10"></a> `00b7db10` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00b7db14"></a> `00b7db14` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b7db18"></a> `00b7db18` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00b7db1c"></a> `00b7db1c` | `1f 05 00 f1` | cmp x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b7db20"></a> `00b7db20` | `68 00 00 54` | b.hi 0x00b7db2c | `CONDITIONAL_JUMP`
<a id="insn-00b7db24"></a> `00b7db24` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-00b7db28"></a> `00b7db28` | `68 36 00 f9` | str x8,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00b7db2c"></a> `00b7db2c` | `68 32 40 b9` | ldr w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7db30"></a> `00b7db30` | `16 01 40 92` | and x22,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b7db34"></a> `00b7db34` | `16 02 00 34` | cbz w22,0x00b7db74 | `CONDITIONAL_JUMP`
<a id="insn-00b7db38"></a> `00b7db38` | `69 22 40 f9` | ldr x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7db3c"></a> `00b7db3c` | `6a 4a 40 b9` | ldr w10,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00b7db40"></a> `00b7db40` | `2a 01 0a 4b` | sub w10,w9,w10 | `FALL_THROUGH`
<a id="insn-00b7db44"></a> `00b7db44` | `5f 01 16 eb` | cmp x10,x22 | `FALL_THROUGH`
<a id="insn-00b7db48"></a> `00b7db48` | `c2 00 00 54` | b.cs 0x00b7db60 | `CONDITIONAL_JUMP`
<a id="insn-00b7db4c"></a> `00b7db4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b7db50"></a> `00b7db50` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b7db54"></a> `00b7db54` | `93 79 03 94` | bl 0x00c5c1a0 | `UNCONDITIONAL_CALL`
<a id="insn-00b7db58"></a> `00b7db58` | `69 22 40 f9` | ldr x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7db5c"></a> `00b7db5c` | `68 32 40 b9` | ldr w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7db60"></a> `00b7db60` | `29 01 16 cb` | sub x9,x9,x22 | `FALL_THROUGH`
<a id="insn-00b7db64"></a> `00b7db64` | `08 01 16 0b` | add w8,w8,w22 | `FALL_THROUGH`
<a id="insn-00b7db68"></a> `00b7db68` | `69 22 00 f9` | str x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7db6c"></a> `00b7db6c` | `68 32 00 b9` | str w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7db70"></a> `00b7db70` | `3f 01 00 39` | strb wzr,[x9] | `FALL_THROUGH`
<a id="insn-00b7db74"></a> `00b7db74` | `69 22 44 a9` | ldp x9,x8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7db78"></a> `00b7db78` | `2a 01 08 4b` | sub w10,w9,w8 | `FALL_THROUGH`
<a id="insn-00b7db7c"></a> `00b7db7c` | `5f 79 7f f2` | tst x10,#0xfffffffe | `FALL_THROUGH`
<a id="insn-00b7db80"></a> `00b7db80` | `a1 00 00 54` | b.ne 0x00b7db94 | `CONDITIONAL_JUMP`
<a id="insn-00b7db84"></a> `00b7db84` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-00b7db88"></a> `00b7db88` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b7db8c"></a> `00b7db8c` | `85 79 03 94` | bl 0x00c5c1a0 | `UNCONDITIONAL_CALL`
<a id="insn-00b7db90"></a> `00b7db90` | `69 22 44 a9` | ldp x9,x8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7db94"></a> `00b7db94` | `6b 32 40 b9` | ldr w11,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7db98"></a> `00b7db98` | `2a 09 00 d1` | sub x10,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00b7db9c"></a> `00b7db9c` | `6a 22 00 f9` | str x10,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7dba0"></a> `00b7dba0` | `4a 01 08 4b` | sub w10,w10,w8 | `FALL_THROUGH`
<a id="insn-00b7dba4"></a> `00b7dba4` | `5f 71 7d f2` | tst x10,#0xfffffff8 | `FALL_THROUGH`
<a id="insn-00b7dba8"></a> `00b7dba8` | `76 09 00 11` | add w22,w11,#0x2 | `FALL_THROUGH`
<a id="insn-00b7dbac"></a> `00b7dbac` | `76 32 00 b9` | str w22,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7dbb0"></a> `00b7dbb0` | `35 e1 1f 78` | sturh w21,[x9, #-0x2] | `FALL_THROUGH`
<a id="insn-00b7dbb4"></a> `00b7dbb4` | `a1 00 00 54` | b.ne 0x00b7dbc8 | `CONDITIONAL_JUMP`
<a id="insn-00b7dbb8"></a> `00b7dbb8` | `01 01 80 52` | mov w1,#0x8 | `FALL_THROUGH`
<a id="insn-00b7dbbc"></a> `00b7dbbc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b7dbc0"></a> `00b7dbc0` | `78 79 03 94` | bl 0x00c5c1a0 | `UNCONDITIONAL_CALL`
<a id="insn-00b7dbc4"></a> `00b7dbc4` | `68 26 40 f9` | ldr x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00b7dbc8"></a> `00b7dbc8` | `89 3e 00 12` | and w9,w20,#0xffff | `FALL_THROUGH`
<a id="insn-00b7dbcc"></a> `00b7dbcc` | `ea 03 16 2a` | mov w10,w22 | `FALL_THROUGH`
<a id="insn-00b7dbd0"></a> `00b7dbd0` | `2a 3d 60 b3` | bfm x10,x9,#0x20,#0xf | `FALL_THROUGH`
<a id="insn-00b7dbd4"></a> `00b7dbd4` | `0a 01 00 f9` | str x10,[x8] | `FALL_THROUGH`
<a id="insn-00b7dbd8"></a> `00b7dbd8` | `68 26 40 f9` | ldr x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00b7dbdc"></a> `00b7dbdc` | `6a 52 40 b9` | ldr w10,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00b7dbe0"></a> `00b7dbe0` | `6b aa 40 79` | ldrh w11,[x19, #0x54] | `FALL_THROUGH`
<a id="insn-00b7dbe4"></a> `00b7dbe4` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00b7dbe8"></a> `00b7dbe8` | `4a 05 00 11` | add w10,w10,#0x1 | `FALL_THROUGH`
<a id="insn-00b7dbec"></a> `00b7dbec` | `7f 01 09 6b` | cmp w11,w9 | `FALL_THROUGH`
<a id="insn-00b7dbf0"></a> `00b7dbf0` | `68 26 00 f9` | str x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00b7dbf4"></a> `00b7dbf4` | `6a 52 00 b9` | str w10,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00b7dbf8"></a> `00b7dbf8` | `42 00 00 54` | b.cs 0x00b7dc00 | `CONDITIONAL_JUMP`
<a id="insn-00b7dbfc"></a> `00b7dbfc` | `74 aa 00 79` | strh w20,[x19, #0x54] | `FALL_THROUGH`
<a id="insn-00b7dc00"></a> `00b7dc00` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b7dc04"></a> `00b7dc04` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7dc08"></a> `00b7dc08` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b7dc0c"></a> `00b7dc0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b7dafc`](#insn-00b7dafc) 範囲 `[['00b7dafc', '00b7db0b']]`
  - `FALL_THROUGH` [`00b7db08`](#insn-00b7db08) → [`00b7db0c`](#insn-00b7db0c)
- ブロック [`00b7db0c`](#insn-00b7db0c) 範囲 `[['00b7db0c', '00b7db13']]`
  - `FALL_THROUGH` [`00b7db10`](#insn-00b7db10) → [`00b7db14`](#insn-00b7db14)
- ブロック [`00b7db14`](#insn-00b7db14) 範囲 `[['00b7db14', '00b7db23']]`
  - `CONDITIONAL_JUMP` [`00b7db20`](#insn-00b7db20) → [`00b7db2c`](#insn-00b7db2c)
  - `FALL_THROUGH` [`00b7db20`](#insn-00b7db20) → [`00b7db24`](#insn-00b7db24)
- ブロック [`00b7db24`](#insn-00b7db24) 範囲 `[['00b7db24', '00b7db2b']]`
  - `FALL_THROUGH` [`00b7db28`](#insn-00b7db28) → [`00b7db2c`](#insn-00b7db2c)
- ブロック [`00b7db2c`](#insn-00b7db2c) 範囲 `[['00b7db2c', '00b7db37']]`
  - `CONDITIONAL_JUMP` [`00b7db34`](#insn-00b7db34) → [`00b7db74`](#insn-00b7db74)
  - `FALL_THROUGH` [`00b7db34`](#insn-00b7db34) → [`00b7db38`](#insn-00b7db38)
- ブロック [`00b7db38`](#insn-00b7db38) 範囲 `[['00b7db38', '00b7db4b']]`
  - `CONDITIONAL_JUMP` [`00b7db48`](#insn-00b7db48) → [`00b7db60`](#insn-00b7db60)
  - `FALL_THROUGH` [`00b7db48`](#insn-00b7db48) → [`00b7db4c`](#insn-00b7db4c)
- ブロック [`00b7db4c`](#insn-00b7db4c) 範囲 `[['00b7db4c', '00b7db5f']]`
  - `FALL_THROUGH` [`00b7db5c`](#insn-00b7db5c) → [`00b7db60`](#insn-00b7db60)
- ブロック [`00b7db60`](#insn-00b7db60) 範囲 `[['00b7db60', '00b7db73']]`
  - `FALL_THROUGH` [`00b7db70`](#insn-00b7db70) → [`00b7db74`](#insn-00b7db74)
- ブロック [`00b7db74`](#insn-00b7db74) 範囲 `[['00b7db74', '00b7db83']]`
  - `CONDITIONAL_JUMP` [`00b7db80`](#insn-00b7db80) → [`00b7db94`](#insn-00b7db94)
  - `FALL_THROUGH` [`00b7db80`](#insn-00b7db80) → [`00b7db84`](#insn-00b7db84)
- ブロック [`00b7db84`](#insn-00b7db84) 範囲 `[['00b7db84', '00b7db93']]`
  - `FALL_THROUGH` [`00b7db90`](#insn-00b7db90) → [`00b7db94`](#insn-00b7db94)
- ブロック [`00b7db94`](#insn-00b7db94) 範囲 `[['00b7db94', '00b7dbb7']]`
  - `CONDITIONAL_JUMP` [`00b7dbb4`](#insn-00b7dbb4) → [`00b7dbc8`](#insn-00b7dbc8)
  - `FALL_THROUGH` [`00b7dbb4`](#insn-00b7dbb4) → [`00b7dbb8`](#insn-00b7dbb8)
- ブロック [`00b7dbb8`](#insn-00b7dbb8) 範囲 `[['00b7dbb8', '00b7dbc7']]`
  - `FALL_THROUGH` [`00b7dbc4`](#insn-00b7dbc4) → [`00b7dbc8`](#insn-00b7dbc8)
- ブロック [`00b7dbc8`](#insn-00b7dbc8) 範囲 `[['00b7dbc8', '00b7dbfb']]`
  - `CONDITIONAL_JUMP` [`00b7dbf8`](#insn-00b7dbf8) → [`00b7dc00`](#insn-00b7dc00)
  - `FALL_THROUGH` [`00b7dbf8`](#insn-00b7dbf8) → [`00b7dbfc`](#insn-00b7dbfc)
- ブロック [`00b7dbfc`](#insn-00b7dbfc) 範囲 `[['00b7dbfc', '00b7dbff']]`
  - `FALL_THROUGH` [`00b7dbfc`](#insn-00b7dbfc) → [`00b7dc00`](#insn-00b7dc00)
- ブロック [`00b7dc00`](#insn-00b7dc00) 範囲 `[['00b7dc00', '00b7dc0f']]`

## 命令位置別の参照

- [`00b7dafc`](#insn-00b7dafc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7db00`](#insn-00b7db00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7db04`](#insn-00b7db04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7db20`](#insn-00b7db20) → [`00b7db2c`](#insn-00b7db2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7db34`](#insn-00b7db34) → [`00b7db74`](#insn-00b7db74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7db48`](#insn-00b7db48) → [`00b7db60`](#insn-00b7db60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7db54`](#insn-00b7db54) → [`00c5c1a0`](../00c5c/00c5c1a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1a0` · 推定シンボル `None` · 推定型 `None`
- [`00b7db80`](#insn-00b7db80) → [`00b7db94`](#insn-00b7db94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7db8c`](#insn-00b7db8c) → [`00c5c1a0`](../00c5c/00c5c1a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1a0` · 推定シンボル `None` · 推定型 `None`
- [`00b7dbb4`](#insn-00b7dbb4) → [`00b7dbc8`](#insn-00b7dbc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7dbc0`](#insn-00b7dbc0) → [`00c5c1a0`](../00c5c/00c5c1a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1a0` · 推定シンボル `None` · 推定型 `None`
- [`00b7dbf8`](#insn-00b7dbf8) → [`00b7dc00`](#insn-00b7dc00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7dc00`](#insn-00b7dc00) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7dc04`](#insn-00b7dc04) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b7dafc`](#insn-00b7dafc)

~~~json
{
  "source": "00b7dafc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7db00`](#insn-00b7db00)

~~~json
{
  "source": "00b7db00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7db04`](#insn-00b7db04)

~~~json
{
  "source": "00b7db04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7db20`](#insn-00b7db20)

~~~json
{
  "source": "00b7db20",
  "target": "00b7db2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7db34`](#insn-00b7db34)

~~~json
{
  "source": "00b7db34",
  "target": "00b7db74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7db48`](#insn-00b7db48)

~~~json
{
  "source": "00b7db48",
  "target": "00b7db60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7db54`](#insn-00b7db54)

~~~json
{
  "source": "00b7db54",
  "target": "00c5c1a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7db80`](#insn-00b7db80)

~~~json
{
  "source": "00b7db80",
  "target": "00b7db94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7db8c`](#insn-00b7db8c)

~~~json
{
  "source": "00b7db8c",
  "target": "00c5c1a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7dbb4`](#insn-00b7dbb4)

~~~json
{
  "source": "00b7dbb4",
  "target": "00b7dbc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7dbc0`](#insn-00b7dbc0)

~~~json
{
  "source": "00b7dbc0",
  "target": "00c5c1a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7dbf8`](#insn-00b7dbf8)

~~~json
{
  "source": "00b7dbf8",
  "target": "00b7dc00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7dc00`](#insn-00b7dc00)

~~~json
{
  "source": "00b7dc00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7dc04`](#insn-00b7dc04)

~~~json
{
  "source": "00b7dc04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
