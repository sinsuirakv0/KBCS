# 00aeac9c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aea874`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea874.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-df907267c75caa588ca9079c791cba2d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aead38`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aea/00aead38.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0065.md#compare-d245b97f6f94b7cc4c8312e8bad84ce5)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeac9c",
  "name": "FUN_00aeac9c",
  "size": 340,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b081b51717d3e81307e8d611378e6c7d3a88e280f7d5e94f0c078cdf0469a1d6",
  "source_text_sha256": "b081b51717d3e81307e8d611378e6c7d3a88e280f7d5e94f0c078cdf0469a1d6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeac9c",
        "00aeadef"
      ]
    ],
    "bytes_sha256": "d88a3e57eb369e52a212006876d841b83fabd993e7a2da6568c9fc5ebb58f78a",
    "instruction_count": 85,
    "instruction_bytes": 340,
    "body_bytes": 340,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [007fb230](../007fb/007fb230.md)
- [0099703c](../00997/0099703c.md)
- [009fd62c](../009fd/009fd62c.md)
- [00a0077c](../00a00/00a0077c.md)
- [00a022d8](../00a02/00a022d8.md)
- [00a03e68](../00a03/00a03e68.md)
- [00ae128c](../00ae1/00ae128c.md)

## 呼び出し先

- [00467860](../00467/00467860.md)
- [00467b2c](../00467/00467b2c.md)
- [00467f54](../00467/00467f54.md)
- [0046c9c4](../0046c/0046c9c4.md)
- [0046ca84](../0046c/0046ca84.md)
- [008514f8](../00851/008514f8.md)
- [00a829d0](../00a82/00a829d0.md)
- [00a83588](../00a83/00a83588.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1601 bytes

~~~c

void FUN_00aeac9c(long param_1,int param_2)

{
  int iVar1;
  int iVar2;
  int iVar3;
  undefined8 uVar4;
  long lVar5;
  
                    /* try { // try from 00aeaca8 to 00beacaf has its CatchHandler @ 00aeaec8 */
  iVar2 = FUN_00a829d0(param_1 + 0x3078,0x65);
  uVar4 = FUN_00467860();
  FUN_008514f8();
  iVar3 = FUN_0046ca84();
  iVar2 = iVar2 * 0x27;
  lVar5 = FUN_008514f8();
  if (param_2 == 0) {
    iVar1 = iVar2;
    if (iVar2 < 0) {
      iVar1 = iVar2 + 1;
    }
                    /* try { // try from 00aead14 to 00bead1b has its CatchHandler @ 00aeaec4 */
    if (iVar3 < 0) {
      iVar3 = iVar3 + 1;
    }
    param_2 = (((iVar3 >> 1) - (iVar1 >> 1)) -
              *(int *)((long)&fde_table_entry_003339e8.initial_loc + lVar5)) + 0x12;
  }
  else {
                    /* try { // try from 00aeacf4 to 00beacff has its CatchHandler @ 00aeaed4 */
    iVar3 = iVar2 + 0x18;
    if (-0x18 < iVar2) {
      iVar3 = iVar2 + 0x17;
    }
    param_2 = param_2 - (iVar3 >> 1);
  }
  FUN_00467b2c(uVar4,0xff,0xff,0xff,0xe6);
  iVar3 = FUN_0046c9c4(param_1);
                    /* try { // try from 00aead60 to 00bead6b has its CatchHandler @ 00aeaecc */
                    /* try { // try from 00aead6c to 00beae97 has its CatchHandler @ 00aea974 */
  FUN_00467f54(uVar4,(int)((double)iVar3 * 0.5 + -430.0),param_2,0x35c,iVar2 + 0x17);
  FUN_00467b2c(uVar4,0,0,0,0xff);
  iVar3 = FUN_0046c9c4(param_1);
  if (iVar3 < 0) {
    iVar3 = iVar3 + 1;
  }
  FUN_00a83588(0x3f800000,param_1 + 0x3078,0x65,iVar3 >> 1,param_2 + 0xd,1);
  FUN_00467b2c(uVar4,0xff,0xff,0xff,0xff);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeac9c"></a> `00aeac9c` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00aeaca0"></a> `00aeaca0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeaca4"></a> `00aeaca4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeaca8"></a> `00aeaca8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aeacac"></a> `00aeacac` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aeacb0"></a> `00aeacb0` | `17 0f 86 52` | mov w23,#0x3078 | `FALL_THROUGH`
<a id="insn-00aeacb4"></a> `00aeacb4` | `f5 03 01 2a` | mov w21,w1 | `FALL_THROUGH`
<a id="insn-00aeacb8"></a> `00aeacb8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aeacbc"></a> `00aeacbc` | `00 00 17 8b` | add x0,x0,x23 | `FALL_THROUGH`
<a id="insn-00aeacc0"></a> `00aeacc0` | `a1 0c 80 52` | mov w1,#0x65 | `FALL_THROUGH`
<a id="insn-00aeacc4"></a> `00aeacc4` | `43 5f fe 97` | bl 0x00a829d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aeacc8"></a> `00aeacc8` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00aeaccc"></a> `00aeaccc` | `e5 f2 e5 97` | bl 0x00467860 | `UNCONDITIONAL_CALL`
<a id="insn-00aeacd0"></a> `00aeacd0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aeacd4"></a> `00aeacd4` | `09 9a f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aeacd8"></a> `00aeacd8` | `6b 07 e6 97` | bl 0x0046ca84 | `UNCONDITIONAL_CALL`
<a id="insn-00aeacdc"></a> `00aeacdc` | `e8 04 80 52` | mov w8,#0x27 | `FALL_THROUGH`
<a id="insn-00aeace0"></a> `00aeace0` | `d8 7e 08 1b` | mul w24,w22,w8 | `FALL_THROUGH`
<a id="insn-00aeace4"></a> `00aeace4` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00aeace8"></a> `00aeace8` | `04 9a f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aeacec"></a> `00aeacec` | `d5 00 00 34` | cbz w21,0x00aead04 | `CONDITIONAL_JUMP`
<a id="insn-00aeacf0"></a> `00aeacf0` | `16 5f 00 31` | adds w22,w24,#0x17 | `FALL_THROUGH`
<a id="insn-00aeacf4"></a> `00aeacf4` | `08 63 00 11` | add w8,w24,#0x18 | `FALL_THROUGH`
<a id="insn-00aeacf8"></a> `00aeacf8` | `08 b1 96 1a` | csel w8,w8,w22,lt | `FALL_THROUGH`
<a id="insn-00aeacfc"></a> `00aeacfc` | `b5 06 88 4b` | sub w21,w21,w8, ASR #0x1 | `FALL_THROUGH`
<a id="insn-00aead00"></a> `00aead00` | `0d 00 00 14` | b 0x00aead34 | `UNCONDITIONAL_JUMP`
<a id="insn-00aead04"></a> `00aead04` | `1f 03 00 71` | cmp w24,#0x0 | `FALL_THROUGH`
<a id="insn-00aead08"></a> `00aead08` | `0a 3d 87 52` | mov w10,#0x39e8 | `FALL_THROUGH`
<a id="insn-00aead0c"></a> `00aead0c` | `08 a7 98 1a` | cinc w8,w24,lt | `FALL_THROUGH`
<a id="insn-00aead10"></a> `00aead10` | `df 02 00 71` | cmp w22,#0x0 | `FALL_THROUGH`
<a id="insn-00aead14"></a> `00aead14` | `6a 06 a0 72` | movk w10,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00aead18"></a> `00aead18` | `c9 a6 96 1a` | cinc w9,w22,lt | `FALL_THROUGH`
<a id="insn-00aead1c"></a> `00aead1c` | `16 5f 00 11` | add w22,w24,#0x17 | `FALL_THROUGH`
<a id="insn-00aead20"></a> `00aead20` | `29 7d 01 13` | asr w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00aead24"></a> `00aead24` | `28 05 88 4b` | sub w8,w9,w8, ASR #0x1 | `FALL_THROUGH`
<a id="insn-00aead28"></a> `00aead28` | `09 68 6a b8` | ldr w9,[x0, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aead2c"></a> `00aead2c` | `08 01 09 4b` | sub w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00aead30"></a> `00aead30` | `15 49 00 11` | add w21,w8,#0x12 | `FALL_THROUGH`
<a id="insn-00aead34"></a> `00aead34` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aead38"></a> `00aead38` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-00aead3c"></a> `00aead3c` | `e2 1f 80 52` | mov w2,#0xff | `FALL_THROUGH`
<a id="insn-00aead40"></a> `00aead40` | `e3 1f 80 52` | mov w3,#0xff | `FALL_THROUGH`
<a id="insn-00aead44"></a> `00aead44` | `c4 1c 80 52` | mov w4,#0xe6 | `FALL_THROUGH`
<a id="insn-00aead48"></a> `00aead48` | `79 f3 e5 97` | bl 0x00467b2c | `UNCONDITIONAL_CALL`
<a id="insn-00aead4c"></a> `00aead4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aead50"></a> `00aead50` | `1d 07 e6 97` | bl 0x0046c9c4 | `UNCONDITIONAL_CALL`
<a id="insn-00aead54"></a> `00aead54` | `08 00 dc d2` | mov x8,#0xe00000000000 | `FALL_THROUGH`
<a id="insn-00aead58"></a> `00aead58` | `00 00 62 1e` | scvtf d0,w0 | `FALL_THROUGH`
<a id="insn-00aead5c"></a> `00aead5c` | `01 10 6c 1e` | fmov d1,0x3fe0000000000000 | `FALL_THROUGH`
<a id="insn-00aead60"></a> `00aead60` | `48 0f f8 f2` | movk x8,#0xc07a, LSL #48 | `FALL_THROUGH`
<a id="insn-00aead64"></a> `00aead64` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aead68"></a> `00aead68` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00aead6c"></a> `00aead6c` | `02 01 67 9e` | fmov d2,x8 | `FALL_THROUGH`
<a id="insn-00aead70"></a> `00aead70` | `83 6b 80 52` | mov w3,#0x35c | `FALL_THROUGH`
<a id="insn-00aead74"></a> `00aead74` | `e4 03 16 2a` | mov w4,w22 | `FALL_THROUGH`
<a id="insn-00aead78"></a> `00aead78` | `00 08 41 1f` | fmadd d0,d0,d1,d2 | `FALL_THROUGH`
<a id="insn-00aead7c"></a> `00aead7c` | `01 00 78 1e` | fcvtzs w1,d0 | `FALL_THROUGH`
<a id="insn-00aead80"></a> `00aead80` | `75 f4 e5 97` | bl 0x00467f54 | `UNCONDITIONAL_CALL`
<a id="insn-00aead84"></a> `00aead84` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aead88"></a> `00aead88` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aead8c"></a> `00aead8c` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aead90"></a> `00aead90` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00aead94"></a> `00aead94` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-00aead98"></a> `00aead98` | `65 f3 e5 97` | bl 0x00467b2c | `UNCONDITIONAL_CALL`
<a id="insn-00aead9c"></a> `00aead9c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeada0"></a> `00aeada0` | `09 07 e6 97` | bl 0x0046c9c4 | `UNCONDITIONAL_CALL`
<a id="insn-00aeada4"></a> `00aeada4` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00aeada8"></a> `00aeada8` | `00 10 2e 1e` | fmov s0,0x3f800000 | `FALL_THROUGH`
<a id="insn-00aeadac"></a> `00aeadac` | `a3 36 00 11` | add w3,w21,#0xd | `FALL_THROUGH`
<a id="insn-00aeadb0"></a> `00aeadb0` | `08 a4 80 1a` | cinc w8,w0,lt | `FALL_THROUGH`
<a id="insn-00aeadb4"></a> `00aeadb4` | `60 02 17 8b` | add x0,x19,x23 | `FALL_THROUGH`
<a id="insn-00aeadb8"></a> `00aeadb8` | `a1 0c 80 52` | mov w1,#0x65 | `FALL_THROUGH`
<a id="insn-00aeadbc"></a> `00aeadbc` | `02 7d 01 13` | asr w2,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aeadc0"></a> `00aeadc0` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-00aeadc4"></a> `00aeadc4` | `f1 61 fe 97` | bl 0x00a83588 | `UNCONDITIONAL_CALL`
<a id="insn-00aeadc8"></a> `00aeadc8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aeadcc"></a> `00aeadcc` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-00aeadd0"></a> `00aeadd0` | `e2 1f 80 52` | mov w2,#0xff | `FALL_THROUGH`
<a id="insn-00aeadd4"></a> `00aeadd4` | `e3 1f 80 52` | mov w3,#0xff | `FALL_THROUGH`
<a id="insn-00aeadd8"></a> `00aeadd8` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-00aeaddc"></a> `00aeaddc` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aeade0"></a> `00aeade0` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeade4"></a> `00aeade4` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeade8"></a> `00aeade8` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00aeadec"></a> `00aeadec` | `50 f3 e5 17` | b 0x00467b2c | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeac9c`](#insn-00aeac9c) 範囲 `[['00aeac9c', '00aeaca7']]`
  - `FALL_THROUGH` [`00aeaca4`](#insn-00aeaca4) → [`00aeaca8`](#insn-00aeaca8)
- ブロック [`00aeaca8`](#insn-00aeaca8) 範囲 `[['00aeaca8', '00aeacef']]`
  - `CONDITIONAL_JUMP` [`00aeacec`](#insn-00aeacec) → [`00aead04`](#insn-00aead04)
  - `FALL_THROUGH` [`00aeacec`](#insn-00aeacec) → [`00aeacf0`](#insn-00aeacf0)
- ブロック [`00aeacf0`](#insn-00aeacf0) 範囲 `[['00aeacf0', '00aeacf3']]`
  - `FALL_THROUGH` [`00aeacf0`](#insn-00aeacf0) → [`00aeacf4`](#insn-00aeacf4)
- ブロック [`00aeacf4`](#insn-00aeacf4) 範囲 `[['00aeacf4', '00aead03']]`
  - `UNCONDITIONAL_JUMP` [`00aead00`](#insn-00aead00) → [`00aead34`](#insn-00aead34)
- ブロック [`00aead04`](#insn-00aead04) 範囲 `[['00aead04', '00aead13']]`
  - `FALL_THROUGH` [`00aead10`](#insn-00aead10) → [`00aead14`](#insn-00aead14)
- ブロック [`00aead14`](#insn-00aead14) 範囲 `[['00aead14', '00aead33']]`
  - `FALL_THROUGH` [`00aead30`](#insn-00aead30) → [`00aead34`](#insn-00aead34)
- ブロック [`00aead34`](#insn-00aead34) 範囲 `[['00aead34', '00aead5f']]`
  - `FALL_THROUGH` [`00aead5c`](#insn-00aead5c) → [`00aead60`](#insn-00aead60)
- ブロック [`00aead60`](#insn-00aead60) 範囲 `[['00aead60', '00aead6b']]`
  - `FALL_THROUGH` [`00aead68`](#insn-00aead68) → [`00aead6c`](#insn-00aead6c)
- ブロック [`00aead6c`](#insn-00aead6c) 範囲 `[['00aead6c', '00aeadef']]`

## 命令位置別の参照

- [`00aeac9c`](#insn-00aeac9c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaca0`](#insn-00aeaca0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaca4`](#insn-00aeaca4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaca8`](#insn-00aeaca8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeacc4`](#insn-00aeacc4) → [`00a829d0`](../00a82/00a829d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a829d0` · 推定シンボル `None` · 推定型 `None`
- [`00aeaccc`](#insn-00aeaccc) → [`00467860`](../00467/00467860.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467860` · 推定シンボル `None` · 推定型 `None`
- [`00aeacd4`](#insn-00aeacd4) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00aeacd8`](#insn-00aeacd8) → [`0046ca84`](../0046c/0046ca84.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca84` · 推定シンボル `None` · 推定型 `None`
- [`00aeace8`](#insn-00aeace8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00aeacec`](#insn-00aeacec) → [`00aead04`](#insn-00aead04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aead00`](#insn-00aead00) → [`00aead34`](#insn-00aead34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aead28`](#insn-00aead28) → `003339e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aead48`](#insn-00aead48) → [`00467b2c`](../00467/00467b2c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467b2c` · 推定シンボル `None` · 推定型 `None`
- [`00aead50`](#insn-00aead50) → [`0046c9c4`](../0046c/0046c9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c9c4` · 推定シンボル `None` · 推定型 `None`
- [`00aead80`](#insn-00aead80) → [`00467f54`](../00467/00467f54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467f54` · 推定シンボル `None` · 推定型 `None`
- [`00aead98`](#insn-00aead98) → [`00467b2c`](../00467/00467b2c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467b2c` · 推定シンボル `None` · 推定型 `None`
- [`00aeada0`](#insn-00aeada0) → [`0046c9c4`](../0046c/0046c9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c9c4` · 推定シンボル `None` · 推定型 `None`
- [`00aeadc4`](#insn-00aeadc4) → [`00a83588`](../00a83/00a83588.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a83588` · 推定シンボル `None` · 推定型 `None`
- [`00aeaddc`](#insn-00aeaddc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeade0`](#insn-00aeade0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeade4`](#insn-00aeade4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeade8`](#insn-00aeade8) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeadec`](#insn-00aeadec) → [`00467b2c`](../00467/00467b2c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467b2c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeac9c`](#insn-00aeac9c)

~~~json
{
  "source": "00aeac9c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaca0`](#insn-00aeaca0)

~~~json
{
  "source": "00aeaca0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaca4`](#insn-00aeaca4)

~~~json
{
  "source": "00aeaca4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaca8`](#insn-00aeaca8)

~~~json
{
  "source": "00aeaca8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeacc4`](#insn-00aeacc4)

~~~json
{
  "source": "00aeacc4",
  "target": "00a829d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeaccc`](#insn-00aeaccc)

~~~json
{
  "source": "00aeaccc",
  "target": "00467860",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeacd4`](#insn-00aeacd4)

~~~json
{
  "source": "00aeacd4",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeacd8`](#insn-00aeacd8)

~~~json
{
  "source": "00aeacd8",
  "target": "0046ca84",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeace8`](#insn-00aeace8)

~~~json
{
  "source": "00aeace8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeacec`](#insn-00aeacec)

~~~json
{
  "source": "00aeacec",
  "target": "00aead04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aead00`](#insn-00aead00)

~~~json
{
  "source": "00aead00",
  "target": "00aead34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aead28`](#insn-00aead28)

~~~json
{
  "source": "00aead28",
  "target": "003339e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003339e8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e4c26a00f4780900",
  "capture_start": "003339e8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aead48`](#insn-00aead48)

~~~json
{
  "source": "00aead48",
  "target": "00467b2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aead50`](#insn-00aead50)

~~~json
{
  "source": "00aead50",
  "target": "0046c9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aead80`](#insn-00aead80)

~~~json
{
  "source": "00aead80",
  "target": "00467f54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aead98`](#insn-00aead98)

~~~json
{
  "source": "00aead98",
  "target": "00467b2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeada0`](#insn-00aeada0)

~~~json
{
  "source": "00aeada0",
  "target": "0046c9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeadc4`](#insn-00aeadc4)

~~~json
{
  "source": "00aeadc4",
  "target": "00a83588",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeaddc`](#insn-00aeaddc)

~~~json
{
  "source": "00aeaddc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeade0`](#insn-00aeade0)

~~~json
{
  "source": "00aeade0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeade4`](#insn-00aeade4)

~~~json
{
  "source": "00aeade4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeade8`](#insn-00aeade8)

~~~json
{
  "source": "00aeade8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeadec`](#insn-00aeadec)

~~~json
{
  "source": "00aeadec",
  "target": "00467b2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
