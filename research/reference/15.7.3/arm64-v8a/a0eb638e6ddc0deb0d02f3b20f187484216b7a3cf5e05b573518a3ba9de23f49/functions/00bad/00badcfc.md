# 00badcfc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00badc34`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bad/00badc34.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0024.md#compare-3221cbcc4237cbc4e87bd0c84570d51e)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00badd40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00badd40.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0023.md#compare-0a0444d499c7e3e0cd371b37c79409f1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00badcfc",
  "name": "FUN_00badcfc",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9282525f3c49fd2b9ebb86b8086689a76fb41d84f58a83f44a1426f99efc928d",
  "source_text_sha256": "9282525f3c49fd2b9ebb86b8086689a76fb41d84f58a83f44a1426f99efc928d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00badcfc",
        "00badde3"
      ]
    ],
    "bytes_sha256": "402ec95bb0f5705ef4d6afc7a8cf4522f737652476739c4cf22ad9f7f6ff918d",
    "instruction_count": 58,
    "instruction_bytes": 232,
    "body_bytes": 232,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00badcdc](../00bad/00badcdc.md)
- [00bae64c](../00bae/00bae64c.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1182 bytes

~~~c

int FUN_00badcfc(ushort *param_1,long param_2,ulong param_3,ulong param_4,uint param_5)

{
  uint uVar1;
  byte bVar2;
  bool bVar3;
  ushort *puVar4;
  ulong uVar5;
  
  puVar4 = param_1;
  if (((1 < param_2 - (long)param_1) && ((param_5 >> 2 & 1) != 0)) && ((char)*param_1 == -1)) {
    puVar4 = param_1 + (*(char *)((long)param_1 + 1) == -2);
  }
  if ((puVar4 < (ushort *)(param_2 + -1)) && (param_3 != 0)) {
    uVar5 = 1;
    do {
      uVar1 = (uint)*puVar4;
      bVar2 = *(byte *)((long)puVar4 + 1) & 0xfc;
      if (bVar2 == 0xd8) {
                    /* try { // try from 00baddcc to 00cade53 has its CatchHandler @ 00badf38 */
        if (((param_2 - (long)puVar4 < 4) || ((*(byte *)((long)puVar4 + 3) & 0xfc) != 0xdc)) ||
           (param_4 < ((uint)(byte)puVar4[1] | (*(byte *)((long)puVar4 + 3) & 3) << 8 |
                      (uVar1 & 0x3ff) << 10) + 0x10000)) break;
        puVar4 = puVar4 + 2;
      }
      else if ((bVar2 == 0xdc) || (puVar4 = puVar4 + (uVar1 <= param_4), param_4 < uVar1)) break;
      bVar3 = uVar5 < param_3;
      uVar5 = uVar5 + 1;
    } while (puVar4 < (ushort *)(param_2 + -1) && bVar3);
  }
  return (int)puVar4 - (int)param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00badcfc"></a> `00badcfc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00badd00"></a> `00badd00` | `28 00 00 cb` | sub x8,x1,x0 | `FALL_THROUGH`
<a id="insn-00badd04"></a> `00badd04` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00badd08"></a> `00badd08` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00badd0c"></a> `00badd0c` | `6b 01 00 54` | b.lt 0x00badd38 | `CONDITIONAL_JUMP`
<a id="insn-00badd10"></a> `00badd10` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00badd14"></a> `00badd14` | `24 01 10 36` | tbz w4,#0x2,0x00badd38 | `CONDITIONAL_JUMP`
<a id="insn-00badd18"></a> `00badd18` | `08 00 40 39` | ldrb w8,[x0] | `FALL_THROUGH`
<a id="insn-00badd1c"></a> `00badd1c` | `1f fd 03 71` | cmp w8,#0xff | `FALL_THROUGH`
<a id="insn-00badd20"></a> `00badd20` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00badd24"></a> `00badd24` | `a1 00 00 54` | b.ne 0x00badd38 | `CONDITIONAL_JUMP`
<a id="insn-00badd28"></a> `00badd28` | `08 04 40 39` | ldrb w8,[x0, #0x1] | `FALL_THROUGH`
<a id="insn-00badd2c"></a> `00badd2c` | `1f f9 03 71` | cmp w8,#0xfe | `FALL_THROUGH`
<a id="insn-00badd30"></a> `00badd30` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00badd34"></a> `00badd34` | `08 44 28 8b` | add x8,x0,w8, UXTW  #0x1 | `FALL_THROUGH`
<a id="insn-00badd38"></a> `00badd38` | `29 04 00 d1` | sub x9,x1,#0x1 | `FALL_THROUGH`
<a id="insn-00badd3c"></a> `00badd3c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00badd40"></a> `00badd40` | `e2 04 00 54` | b.cs 0x00badddc | `CONDITIONAL_JUMP`
<a id="insn-00badd44"></a> `00badd44` | `c2 04 00 b4` | cbz x2,0x00badddc | `CONDITIONAL_JUMP`
<a id="insn-00badd48"></a> `00badd48` | `2a 00 80 52` | mov w10,#0x1 | `FALL_THROUGH`
<a id="insn-00badd4c"></a> `00badd4c` | `0b 00 9b 52` | mov w11,#0xd800 | `FALL_THROUGH`
<a id="insn-00badd50"></a> `00badd50` | `0c 80 9b 52` | mov w12,#0xdc00 | `FALL_THROUGH`
<a id="insn-00badd54"></a> `00badd54` | `05 00 00 14` | b 0x00badd68 | `UNCONDITIONAL_JUMP`
<a id="insn-00badd58"></a> `00badd58` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00badd5c"></a> `00badd5c` | `42 31 42 fa` | ccmp x10,x2,#0x2,cc | `FALL_THROUGH`
<a id="insn-00badd60"></a> `00badd60` | `4a 05 00 91` | add x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00badd64"></a> `00badd64` | `c2 03 00 54` | b.cs 0x00badddc | `CONDITIONAL_JUMP`
<a id="insn-00badd68"></a> `00badd68` | `0f 05 40 39` | ldrb w15,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00badd6c"></a> `00badd6c` | `0d 01 40 39` | ldrb w13,[x8] | `FALL_THROUGH`
<a id="insn-00badd70"></a> `00badd70` | `ee 5d 18 53` | lsl w14,w15,#0x8 | `FALL_THROUGH`
<a id="insn-00badd74"></a> `00badd74` | `ed 1d 18 33` | bfm w13,w15,#0x18,#0x7 | `FALL_THROUGH`
<a id="insn-00badd78"></a> `00badd78` | `ce 15 16 12` | and w14,w14,#0xfc00 | `FALL_THROUGH`
<a id="insn-00badd7c"></a> `00badd7c` | `df 01 0b 6b` | cmp w14,w11 | `FALL_THROUGH`
<a id="insn-00badd80"></a> `00badd80` | `00 01 00 54` | b.eq 0x00badda0 | `CONDITIONAL_JUMP`
<a id="insn-00badd84"></a> `00badd84` | `df 01 0c 6b` | cmp w14,w12 | `FALL_THROUGH`
<a id="insn-00badd88"></a> `00badd88` | `a0 02 00 54` | b.eq 0x00badddc | `CONDITIONAL_JUMP`
<a id="insn-00badd8c"></a> `00badd8c` | `bf 01 03 eb` | cmp x13,x3 | `FALL_THROUGH`
<a id="insn-00badd90"></a> `00badd90` | `ed 87 9f 1a` | cset w13,ls | `FALL_THROUGH`
<a id="insn-00badd94"></a> `00badd94` | `08 45 2d 8b` | add x8,x8,w13, UXTW  #0x1 | `FALL_THROUGH`
<a id="insn-00badd98"></a> `00badd98` | `09 fe ff 54` | b.ls 0x00badd58 | `CONDITIONAL_JUMP`
<a id="insn-00badd9c"></a> `00badd9c` | `10 00 00 14` | b 0x00badddc | `UNCONDITIONAL_JUMP`
<a id="insn-00badda0"></a> `00badda0` | `2e 00 08 cb` | sub x14,x1,x8 | `FALL_THROUGH`
<a id="insn-00badda4"></a> `00badda4` | `df 11 00 f1` | cmp x14,#0x4 | `FALL_THROUGH`
<a id="insn-00badda8"></a> `00badda8` | `ab 01 00 54` | b.lt 0x00badddc | `CONDITIONAL_JUMP`
<a id="insn-00baddac"></a> `00baddac` | `0e 0d 40 39` | ldrb w14,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00baddb0"></a> `00baddb0` | `cf 15 1e 12` | and w15,w14,#0xfc | `FALL_THROUGH`
<a id="insn-00baddb4"></a> `00baddb4` | `ff 71 03 71` | cmp w15,#0xdc | `FALL_THROUGH`
<a id="insn-00baddb8"></a> `00baddb8` | `21 01 00 54` | b.ne 0x00badddc | `CONDITIONAL_JUMP`
<a id="insn-00baddbc"></a> `00baddbc` | `0f 09 40 39` | ldrb w15,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00baddc0"></a> `00baddc0` | `cf 05 18 33` | bfm w15,w14,#0x18,#0x1 | `FALL_THROUGH`
<a id="insn-00baddc4"></a> `00baddc4` | `af 25 16 33` | bfm w15,w13,#0x16,#0x9 | `FALL_THROUGH`
<a id="insn-00baddc8"></a> `00baddc8` | `ed 41 40 11` | add w13,w15,#0x10, LSL #12 | `FALL_THROUGH`
<a id="insn-00baddcc"></a> `00baddcc` | `bf 01 03 eb` | cmp x13,x3 | `FALL_THROUGH`
<a id="insn-00baddd0"></a> `00baddd0` | `68 00 00 54` | b.hi 0x00badddc | `CONDITIONAL_JUMP`
<a id="insn-00baddd4"></a> `00baddd4` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00baddd8"></a> `00baddd8` | `e0 ff ff 17` | b 0x00badd58 | `UNCONDITIONAL_JUMP`
<a id="insn-00badddc"></a> `00badddc` | `00 01 00 4b` | sub w0,w8,w0 | `FALL_THROUGH`
<a id="insn-00badde0"></a> `00badde0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00badcfc`](#insn-00badcfc) 範囲 `[['00badcfc', '00badd0f']]`
  - `CONDITIONAL_JUMP` [`00badd0c`](#insn-00badd0c) → [`00badd38`](#insn-00badd38)
  - `FALL_THROUGH` [`00badd0c`](#insn-00badd0c) → [`00badd10`](#insn-00badd10)
- ブロック [`00badd10`](#insn-00badd10) 範囲 `[['00badd10', '00badd17']]`
  - `CONDITIONAL_JUMP` [`00badd14`](#insn-00badd14) → [`00badd38`](#insn-00badd38)
  - `FALL_THROUGH` [`00badd14`](#insn-00badd14) → [`00badd18`](#insn-00badd18)
- ブロック [`00badd18`](#insn-00badd18) 範囲 `[['00badd18', '00badd27']]`
  - `CONDITIONAL_JUMP` [`00badd24`](#insn-00badd24) → [`00badd38`](#insn-00badd38)
  - `FALL_THROUGH` [`00badd24`](#insn-00badd24) → [`00badd28`](#insn-00badd28)
- ブロック [`00badd28`](#insn-00badd28) 範囲 `[['00badd28', '00badd37']]`
  - `FALL_THROUGH` [`00badd34`](#insn-00badd34) → [`00badd38`](#insn-00badd38)
- ブロック [`00badd38`](#insn-00badd38) 範囲 `[['00badd38', '00badd43']]`
  - `CONDITIONAL_JUMP` [`00badd40`](#insn-00badd40) → [`00badddc`](#insn-00badddc)
  - `FALL_THROUGH` [`00badd40`](#insn-00badd40) → [`00badd44`](#insn-00badd44)
- ブロック [`00badd44`](#insn-00badd44) 範囲 `[['00badd44', '00badd47']]`
  - `CONDITIONAL_JUMP` [`00badd44`](#insn-00badd44) → [`00badddc`](#insn-00badddc)
  - `FALL_THROUGH` [`00badd44`](#insn-00badd44) → [`00badd48`](#insn-00badd48)
- ブロック [`00badd48`](#insn-00badd48) 範囲 `[['00badd48', '00badd57']]`
  - `UNCONDITIONAL_JUMP` [`00badd54`](#insn-00badd54) → [`00badd68`](#insn-00badd68)
- ブロック [`00badd58`](#insn-00badd58) 範囲 `[['00badd58', '00badd67']]`
  - `CONDITIONAL_JUMP` [`00badd64`](#insn-00badd64) → [`00badddc`](#insn-00badddc)
  - `FALL_THROUGH` [`00badd64`](#insn-00badd64) → [`00badd68`](#insn-00badd68)
- ブロック [`00badd68`](#insn-00badd68) 範囲 `[['00badd68', '00badd83']]`
  - `CONDITIONAL_JUMP` [`00badd80`](#insn-00badd80) → [`00badda0`](#insn-00badda0)
  - `FALL_THROUGH` [`00badd80`](#insn-00badd80) → [`00badd84`](#insn-00badd84)
- ブロック [`00badd84`](#insn-00badd84) 範囲 `[['00badd84', '00badd8b']]`
  - `CONDITIONAL_JUMP` [`00badd88`](#insn-00badd88) → [`00badddc`](#insn-00badddc)
  - `FALL_THROUGH` [`00badd88`](#insn-00badd88) → [`00badd8c`](#insn-00badd8c)
- ブロック [`00badd8c`](#insn-00badd8c) 範囲 `[['00badd8c', '00badd9b']]`
  - `CONDITIONAL_JUMP` [`00badd98`](#insn-00badd98) → [`00badd58`](#insn-00badd58)
  - `FALL_THROUGH` [`00badd98`](#insn-00badd98) → [`00badd9c`](#insn-00badd9c)
- ブロック [`00badd9c`](#insn-00badd9c) 範囲 `[['00badd9c', '00badd9f']]`
  - `UNCONDITIONAL_JUMP` [`00badd9c`](#insn-00badd9c) → [`00badddc`](#insn-00badddc)
- ブロック [`00badda0`](#insn-00badda0) 範囲 `[['00badda0', '00baddab']]`
  - `CONDITIONAL_JUMP` [`00badda8`](#insn-00badda8) → [`00badddc`](#insn-00badddc)
  - `FALL_THROUGH` [`00badda8`](#insn-00badda8) → [`00baddac`](#insn-00baddac)
- ブロック [`00baddac`](#insn-00baddac) 範囲 `[['00baddac', '00baddbb']]`
  - `CONDITIONAL_JUMP` [`00baddb8`](#insn-00baddb8) → [`00badddc`](#insn-00badddc)
  - `FALL_THROUGH` [`00baddb8`](#insn-00baddb8) → [`00baddbc`](#insn-00baddbc)
- ブロック [`00baddbc`](#insn-00baddbc) 範囲 `[['00baddbc', '00baddcb']]`
  - `FALL_THROUGH` [`00baddc8`](#insn-00baddc8) → [`00baddcc`](#insn-00baddcc)
- ブロック [`00baddcc`](#insn-00baddcc) 範囲 `[['00baddcc', '00baddd3']]`
  - `CONDITIONAL_JUMP` [`00baddd0`](#insn-00baddd0) → [`00badddc`](#insn-00badddc)
  - `FALL_THROUGH` [`00baddd0`](#insn-00baddd0) → [`00baddd4`](#insn-00baddd4)
- ブロック [`00baddd4`](#insn-00baddd4) 範囲 `[['00baddd4', '00badddb']]`
  - `UNCONDITIONAL_JUMP` [`00baddd8`](#insn-00baddd8) → [`00badd58`](#insn-00badd58)
- ブロック [`00badddc`](#insn-00badddc) 範囲 `[['00badddc', '00badde3']]`

## 命令位置別の参照

- [`00badd0c`](#insn-00badd0c) → [`00badd38`](#insn-00badd38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badd14`](#insn-00badd14) → [`00badd38`](#insn-00badd38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badd24`](#insn-00badd24) → [`00badd38`](#insn-00badd38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badd40`](#insn-00badd40) → [`00badddc`](#insn-00badddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badd44`](#insn-00badd44) → [`00badddc`](#insn-00badddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badd54`](#insn-00badd54) → [`00badd68`](#insn-00badd68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badd64`](#insn-00badd64) → [`00badddc`](#insn-00badddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badd80`](#insn-00badd80) → [`00badda0`](#insn-00badda0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badd88`](#insn-00badd88) → [`00badddc`](#insn-00badddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badd98`](#insn-00badd98) → [`00badd58`](#insn-00badd58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badd9c`](#insn-00badd9c) → [`00badddc`](#insn-00badddc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badda8`](#insn-00badda8) → [`00badddc`](#insn-00badddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baddb8`](#insn-00baddb8) → [`00badddc`](#insn-00badddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baddd0`](#insn-00baddd0) → [`00badddc`](#insn-00badddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baddd8`](#insn-00baddd8) → [`00badd58`](#insn-00badd58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00badd0c`](#insn-00badd0c)

~~~json
{
  "source": "00badd0c",
  "target": "00badd38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badd14`](#insn-00badd14)

~~~json
{
  "source": "00badd14",
  "target": "00badd38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badd24`](#insn-00badd24)

~~~json
{
  "source": "00badd24",
  "target": "00badd38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badd40`](#insn-00badd40)

~~~json
{
  "source": "00badd40",
  "target": "00badddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badd44`](#insn-00badd44)

~~~json
{
  "source": "00badd44",
  "target": "00badddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badd54`](#insn-00badd54)

~~~json
{
  "source": "00badd54",
  "target": "00badd68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badd64`](#insn-00badd64)

~~~json
{
  "source": "00badd64",
  "target": "00badddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badd80`](#insn-00badd80)

~~~json
{
  "source": "00badd80",
  "target": "00badda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badd88`](#insn-00badd88)

~~~json
{
  "source": "00badd88",
  "target": "00badddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badd98`](#insn-00badd98)

~~~json
{
  "source": "00badd98",
  "target": "00badd58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badd9c`](#insn-00badd9c)

~~~json
{
  "source": "00badd9c",
  "target": "00badddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badda8`](#insn-00badda8)

~~~json
{
  "source": "00badda8",
  "target": "00badddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baddb8`](#insn-00baddb8)

~~~json
{
  "source": "00baddb8",
  "target": "00badddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baddd0`](#insn-00baddd0)

~~~json
{
  "source": "00baddd0",
  "target": "00badddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baddd8`](#insn-00baddd8)

~~~json
{
  "source": "00baddd8",
  "target": "00badd58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
