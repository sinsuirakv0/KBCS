# 00aef8cc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aef4a4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef4a4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0065.md#compare-0880e83042df06252c7904f02bed1072)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aef968`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aef968.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0066.md#compare-ddf6cc20e7f070e5f99f493c245895c5)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aef8cc",
  "name": "FUN_00aef8cc",
  "size": 228,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "36d14bd72d07d817a6ff1a30ec311b29457ced7c852c66feb94b5a40844b3d3c",
  "source_text_sha256": "36d14bd72d07d817a6ff1a30ec311b29457ced7c852c66feb94b5a40844b3d3c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aef8cc",
        "00aef9af"
      ]
    ],
    "bytes_sha256": "ca37470cc0d76881a0776cad8962b160ba317ab11ed7e3db27f2ca5fa262a13c",
    "instruction_count": 57,
    "instruction_bytes": 228,
    "body_bytes": 228,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [008b6f18](../008b6/008b6f18.md)
- [008b79c8](../008b7/008b79c8.md)
- [008b9178](../008b9/008b9178.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2084 bytes

~~~c

void FUN_00aef8cc(long param_1,undefined8 *param_2,int *param_3,uint *param_4)

{
  int iVar1;
  uint uVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined4 uVar5;
  long lVar6;
  
  iVar1 = *param_3;
  uVar2 = *param_4;
                    /* try { // try from 00aef8e0 to 00bef95f has its CatchHandler @ 00aef8e0
                       catch() { ... } // from try @ 00aef8e0 with catch @ 00aef8e0
                       catch() { ... } // from try @ 00aef968 with catch @ 00aef8e0
                       catch() { ... } // from try @ 00aef9e0 with catch @ 00aef8e0
                       catch() { ... } // from try @ 00aefa58 with catch @ 00aef8e0
                       catch() { ... } // from try @ 00aefad0 with catch @ 00aef8e0
                       catch() { ... } // from try @ 00aefb50 with catch @ 00aef8e0
                       catch() { ... } // from try @ 00aefbd0 with catch @ 00aef8e0
                       catch() { ... } // from try @ 00aefc4c with catch @ 00aef8e0
                       catch() { ... } // from try @ 00aefd9c with catch @ 00aef8e0 */
  lVar6 = *(long *)(param_1 + 8);
  if (iVar1 == 5) {
    if (uVar2 < 2) {
      uVar3 = FUN_0047acf4();
      FUN_0047cdd4(uVar3,0xb,0);
      *(int *)(lVar6 + 0x1188) = *(int *)(lVar6 + 0x1188) + 1;
      if (uVar2 == 0) {
        uVar5 = 1;
      }
      else {
        uVar5 = 2;
      }
      *(undefined4 *)(lVar6 + 0x118c) = uVar5;
    }
  }
  else if (iVar1 == 3) {
    if (uVar2 < 2) {
      uVar3 = FUN_0047acf4();
                    /* try { // try from 00aef960 to 00bef967 has its CatchHandler @ 00aefdb8 */
                    /* try { // try from 00aef968 to 00bef9d7 has its CatchHandler @ 00aef8e0 */
      FUN_0047cdd4(uVar3,0xf,0);
      return;
    }
  }
  else if (iVar1 == 2) {
    uVar3 = *param_2;
    if (1 < uVar2) {
      if (uVar2 != 0xfffffffe) {
        return;
      }
      uVar4 = FUN_0047acf4(uVar3);
      FUN_0047cdd4(uVar4,0xb,0);
    }
    FUN_008b9178(uVar3);
    uVar3 = FUN_008b79c8(lVar6 + 0x2f38,0x326);
    FUN_008b6f18(uVar3,0);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aef8cc"></a> `00aef8cc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aef8d0"></a> `00aef8d0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aef8d4"></a> `00aef8d4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aef8d8"></a> `00aef8d8` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00aef8dc"></a> `00aef8dc` | `73 00 40 b9` | ldr w19,[x3] | `FALL_THROUGH`
<a id="insn-00aef8e0"></a> `00aef8e0` | `14 04 40 f9` | ldr x20,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aef8e4"></a> `00aef8e4` | `1f 15 00 71` | cmp w8,#0x5 | `FALL_THROUGH`
<a id="insn-00aef8e8"></a> `00aef8e8` | `20 04 00 54` | b.eq 0x00aef96c | `CONDITIONAL_JUMP`
<a id="insn-00aef8ec"></a> `00aef8ec` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00aef8f0"></a> `00aef8f0` | `e0 02 00 54` | b.eq 0x00aef94c | `CONDITIONAL_JUMP`
<a id="insn-00aef8f4"></a> `00aef8f4` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00aef8f8"></a> `00aef8f8` | `61 05 00 54` | b.ne 0x00aef9a4 | `CONDITIONAL_JUMP`
<a id="insn-00aef8fc"></a> `00aef8fc` | `20 00 40 f9` | ldr x0,[x1] | `FALL_THROUGH`
<a id="insn-00aef900"></a> `00aef900` | `7f 06 00 71` | cmp w19,#0x1 | `FALL_THROUGH`
<a id="insn-00aef904"></a> `00aef904` | `29 01 00 54` | b.ls 0x00aef928 | `CONDITIONAL_JUMP`
<a id="insn-00aef908"></a> `00aef908` | `7f 0a 00 31` | cmn w19,#0x2 | `FALL_THROUGH`
<a id="insn-00aef90c"></a> `00aef90c` | `c1 04 00 54` | b.ne 0x00aef9a4 | `CONDITIONAL_JUMP`
<a id="insn-00aef910"></a> `00aef910` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aef914"></a> `00aef914` | `f8 2c e6 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-00aef918"></a> `00aef918` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00aef91c"></a> `00aef91c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aef920"></a> `00aef920` | `2d 35 e6 97` | bl 0x0047cdd4 | `UNCONDITIONAL_CALL`
<a id="insn-00aef924"></a> `00aef924` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aef928"></a> `00aef928` | `14 26 f7 97` | bl 0x008b9178 | `UNCONDITIONAL_CALL`
<a id="insn-00aef92c"></a> `00aef92c` | `08 e7 85 52` | mov w8,#0x2f38 | `FALL_THROUGH`
<a id="insn-00aef930"></a> `00aef930` | `c1 64 80 52` | mov w1,#0x326 | `FALL_THROUGH`
<a id="insn-00aef934"></a> `00aef934` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00aef938"></a> `00aef938` | `24 20 f7 97` | bl 0x008b79c8 | `UNCONDITIONAL_CALL`
<a id="insn-00aef93c"></a> `00aef93c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aef940"></a> `00aef940` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aef944"></a> `00aef944` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aef948"></a> `00aef948` | `74 1d f7 17` | b 0x008b6f18 | `CALL_TERMINATOR`
<a id="insn-00aef94c"></a> `00aef94c` | `7f 06 00 71` | cmp w19,#0x1 | `FALL_THROUGH`
<a id="insn-00aef950"></a> `00aef950` | `a8 02 00 54` | b.hi 0x00aef9a4 | `CONDITIONAL_JUMP`
<a id="insn-00aef954"></a> `00aef954` | `e8 2c e6 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-00aef958"></a> `00aef958` | `e1 01 80 52` | mov w1,#0xf | `FALL_THROUGH`
<a id="insn-00aef95c"></a> `00aef95c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aef960"></a> `00aef960` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aef964"></a> `00aef964` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aef968"></a> `00aef968` | `1b 35 e6 17` | b 0x0047cdd4 | `CALL_TERMINATOR`
<a id="insn-00aef96c"></a> `00aef96c` | `7f 06 00 71` | cmp w19,#0x1 | `FALL_THROUGH`
<a id="insn-00aef970"></a> `00aef970` | `a8 01 00 54` | b.hi 0x00aef9a4 | `CONDITIONAL_JUMP`
<a id="insn-00aef974"></a> `00aef974` | `e0 2c e6 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-00aef978"></a> `00aef978` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00aef97c"></a> `00aef97c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aef980"></a> `00aef980` | `15 35 e6 97` | bl 0x0047cdd4 | `UNCONDITIONAL_CALL`
<a id="insn-00aef984"></a> `00aef984` | `88 8a 51 b9` | ldr w8,[x20, #0x1188] | `FALL_THROUGH`
<a id="insn-00aef988"></a> `00aef988` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aef98c"></a> `00aef98c` | `88 8a 11 b9` | str w8,[x20, #0x1188] | `FALL_THROUGH`
<a id="insn-00aef990"></a> `00aef990` | `73 00 00 34` | cbz w19,0x00aef99c | `CONDITIONAL_JUMP`
<a id="insn-00aef994"></a> `00aef994` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-00aef998"></a> `00aef998` | `02 00 00 14` | b 0x00aef9a0 | `UNCONDITIONAL_JUMP`
<a id="insn-00aef99c"></a> `00aef99c` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aef9a0"></a> `00aef9a0` | `88 8e 11 b9` | str w8,[x20, #0x118c] | `FALL_THROUGH`
<a id="insn-00aef9a4"></a> `00aef9a4` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aef9a8"></a> `00aef9a8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aef9ac"></a> `00aef9ac` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aef8cc`](#insn-00aef8cc) 範囲 `[['00aef8cc', '00aef8df']]`
  - `FALL_THROUGH` [`00aef8dc`](#insn-00aef8dc) → [`00aef8e0`](#insn-00aef8e0)
- ブロック [`00aef8e0`](#insn-00aef8e0) 範囲 `[['00aef8e0', '00aef8eb']]`
  - `CONDITIONAL_JUMP` [`00aef8e8`](#insn-00aef8e8) → [`00aef96c`](#insn-00aef96c)
  - `FALL_THROUGH` [`00aef8e8`](#insn-00aef8e8) → [`00aef8ec`](#insn-00aef8ec)
- ブロック [`00aef8ec`](#insn-00aef8ec) 範囲 `[['00aef8ec', '00aef8f3']]`
  - `CONDITIONAL_JUMP` [`00aef8f0`](#insn-00aef8f0) → [`00aef94c`](#insn-00aef94c)
  - `FALL_THROUGH` [`00aef8f0`](#insn-00aef8f0) → [`00aef8f4`](#insn-00aef8f4)
- ブロック [`00aef8f4`](#insn-00aef8f4) 範囲 `[['00aef8f4', '00aef8fb']]`
  - `CONDITIONAL_JUMP` [`00aef8f8`](#insn-00aef8f8) → [`00aef9a4`](#insn-00aef9a4)
  - `FALL_THROUGH` [`00aef8f8`](#insn-00aef8f8) → [`00aef8fc`](#insn-00aef8fc)
- ブロック [`00aef8fc`](#insn-00aef8fc) 範囲 `[['00aef8fc', '00aef907']]`
  - `CONDITIONAL_JUMP` [`00aef904`](#insn-00aef904) → [`00aef928`](#insn-00aef928)
  - `FALL_THROUGH` [`00aef904`](#insn-00aef904) → [`00aef908`](#insn-00aef908)
- ブロック [`00aef908`](#insn-00aef908) 範囲 `[['00aef908', '00aef90f']]`
  - `CONDITIONAL_JUMP` [`00aef90c`](#insn-00aef90c) → [`00aef9a4`](#insn-00aef9a4)
  - `FALL_THROUGH` [`00aef90c`](#insn-00aef90c) → [`00aef910`](#insn-00aef910)
- ブロック [`00aef910`](#insn-00aef910) 範囲 `[['00aef910', '00aef927']]`
  - `FALL_THROUGH` [`00aef924`](#insn-00aef924) → [`00aef928`](#insn-00aef928)
- ブロック [`00aef928`](#insn-00aef928) 範囲 `[['00aef928', '00aef94b']]`
- ブロック [`00aef94c`](#insn-00aef94c) 範囲 `[['00aef94c', '00aef953']]`
  - `CONDITIONAL_JUMP` [`00aef950`](#insn-00aef950) → [`00aef9a4`](#insn-00aef9a4)
  - `FALL_THROUGH` [`00aef950`](#insn-00aef950) → [`00aef954`](#insn-00aef954)
- ブロック [`00aef954`](#insn-00aef954) 範囲 `[['00aef954', '00aef95f']]`
  - `FALL_THROUGH` [`00aef95c`](#insn-00aef95c) → [`00aef960`](#insn-00aef960)
- ブロック [`00aef960`](#insn-00aef960) 範囲 `[['00aef960', '00aef967']]`
  - `FALL_THROUGH` [`00aef964`](#insn-00aef964) → [`00aef968`](#insn-00aef968)
- ブロック [`00aef968`](#insn-00aef968) 範囲 `[['00aef968', '00aef96b']]`
- ブロック [`00aef96c`](#insn-00aef96c) 範囲 `[['00aef96c', '00aef973']]`
  - `CONDITIONAL_JUMP` [`00aef970`](#insn-00aef970) → [`00aef9a4`](#insn-00aef9a4)
  - `FALL_THROUGH` [`00aef970`](#insn-00aef970) → [`00aef974`](#insn-00aef974)
- ブロック [`00aef974`](#insn-00aef974) 範囲 `[['00aef974', '00aef993']]`
  - `CONDITIONAL_JUMP` [`00aef990`](#insn-00aef990) → [`00aef99c`](#insn-00aef99c)
  - `FALL_THROUGH` [`00aef990`](#insn-00aef990) → [`00aef994`](#insn-00aef994)
- ブロック [`00aef994`](#insn-00aef994) 範囲 `[['00aef994', '00aef99b']]`
  - `UNCONDITIONAL_JUMP` [`00aef998`](#insn-00aef998) → [`00aef9a0`](#insn-00aef9a0)
- ブロック [`00aef99c`](#insn-00aef99c) 範囲 `[['00aef99c', '00aef99f']]`
  - `FALL_THROUGH` [`00aef99c`](#insn-00aef99c) → [`00aef9a0`](#insn-00aef9a0)
- ブロック [`00aef9a0`](#insn-00aef9a0) 範囲 `[['00aef9a0', '00aef9a3']]`
  - `FALL_THROUGH` [`00aef9a0`](#insn-00aef9a0) → [`00aef9a4`](#insn-00aef9a4)
- ブロック [`00aef9a4`](#insn-00aef9a4) 範囲 `[['00aef9a4', '00aef9af']]`

## 命令位置別の参照

- [`00aef8cc`](#insn-00aef8cc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aef8d0`](#insn-00aef8d0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aef8e8`](#insn-00aef8e8) → [`00aef96c`](#insn-00aef96c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aef8f0`](#insn-00aef8f0) → [`00aef94c`](#insn-00aef94c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aef8f8`](#insn-00aef8f8) → [`00aef9a4`](#insn-00aef9a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aef904`](#insn-00aef904) → [`00aef928`](#insn-00aef928) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aef90c`](#insn-00aef90c) → [`00aef9a4`](#insn-00aef9a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aef914`](#insn-00aef914) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`00aef920`](#insn-00aef920) → [`0047cdd4`](../0047c/0047cdd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cdd4` · 推定シンボル `None` · 推定型 `None`
- [`00aef928`](#insn-00aef928) → [`008b9178`](../008b9/008b9178.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9178` · 推定シンボル `None` · 推定型 `None`
- [`00aef938`](#insn-00aef938) → [`008b79c8`](../008b7/008b79c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b79c8` · 推定シンボル `None` · 推定型 `None`
- [`00aef940`](#insn-00aef940) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aef944`](#insn-00aef944) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aef948`](#insn-00aef948) → [`008b6f18`](../008b6/008b6f18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6f18` · 推定シンボル `None` · 推定型 `None`
- [`00aef950`](#insn-00aef950) → [`00aef9a4`](#insn-00aef9a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aef954`](#insn-00aef954) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`00aef960`](#insn-00aef960) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aef964`](#insn-00aef964) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aef968`](#insn-00aef968) → [`0047cdd4`](../0047c/0047cdd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cdd4` · 推定シンボル `None` · 推定型 `None`
- [`00aef970`](#insn-00aef970) → [`00aef9a4`](#insn-00aef9a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aef974`](#insn-00aef974) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`00aef980`](#insn-00aef980) → [`0047cdd4`](../0047c/0047cdd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cdd4` · 推定シンボル `None` · 推定型 `None`
- [`00aef990`](#insn-00aef990) → [`00aef99c`](#insn-00aef99c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aef998`](#insn-00aef998) → [`00aef9a0`](#insn-00aef9a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aef9a4`](#insn-00aef9a4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aef9a8`](#insn-00aef9a8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aef8cc`](#insn-00aef8cc)

~~~json
{
  "source": "00aef8cc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aef8d0`](#insn-00aef8d0)

~~~json
{
  "source": "00aef8d0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aef8e8`](#insn-00aef8e8)

~~~json
{
  "source": "00aef8e8",
  "target": "00aef96c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aef8f0`](#insn-00aef8f0)

~~~json
{
  "source": "00aef8f0",
  "target": "00aef94c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aef8f8`](#insn-00aef8f8)

~~~json
{
  "source": "00aef8f8",
  "target": "00aef9a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aef904`](#insn-00aef904)

~~~json
{
  "source": "00aef904",
  "target": "00aef928",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aef90c`](#insn-00aef90c)

~~~json
{
  "source": "00aef90c",
  "target": "00aef9a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aef914`](#insn-00aef914)

~~~json
{
  "source": "00aef914",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aef920`](#insn-00aef920)

~~~json
{
  "source": "00aef920",
  "target": "0047cdd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aef928`](#insn-00aef928)

~~~json
{
  "source": "00aef928",
  "target": "008b9178",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aef938`](#insn-00aef938)

~~~json
{
  "source": "00aef938",
  "target": "008b79c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aef940`](#insn-00aef940)

~~~json
{
  "source": "00aef940",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aef944`](#insn-00aef944)

~~~json
{
  "source": "00aef944",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aef948`](#insn-00aef948)

~~~json
{
  "source": "00aef948",
  "target": "008b6f18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aef950`](#insn-00aef950)

~~~json
{
  "source": "00aef950",
  "target": "00aef9a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aef954`](#insn-00aef954)

~~~json
{
  "source": "00aef954",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aef960`](#insn-00aef960)

~~~json
{
  "source": "00aef960",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aef964`](#insn-00aef964)

~~~json
{
  "source": "00aef964",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aef968`](#insn-00aef968)

~~~json
{
  "source": "00aef968",
  "target": "0047cdd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aef970`](#insn-00aef970)

~~~json
{
  "source": "00aef970",
  "target": "00aef9a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aef974`](#insn-00aef974)

~~~json
{
  "source": "00aef974",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aef980`](#insn-00aef980)

~~~json
{
  "source": "00aef980",
  "target": "0047cdd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aef990`](#insn-00aef990)

~~~json
{
  "source": "00aef990",
  "target": "00aef99c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aef998`](#insn-00aef998)

~~~json
{
  "source": "00aef998",
  "target": "00aef9a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aef9a4`](#insn-00aef9a4)

~~~json
{
  "source": "00aef9a4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aef9a8`](#insn-00aef9a8)

~~~json
{
  "source": "00aef9a8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
