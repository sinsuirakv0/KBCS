# 00afa8fc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afa9c4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa9c4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-a323658ab60d06166cfb01567c9659cf)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afa8fc",
  "name": "FUN_00afa8fc",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "414d41168417aa30ae0fffaedda18bcf21a9f2fa414448a6e80b6a72f18cd5ae",
  "source_text_sha256": "414d41168417aa30ae0fffaedda18bcf21a9f2fa414448a6e80b6a72f18cd5ae",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afa8fc",
        "00afa9e3"
      ]
    ],
    "bytes_sha256": "85f61a29801ce18e1ddc91ceba52cca12e22079d4fd662fe7197e2e7bf47e55a",
    "instruction_count": 58,
    "instruction_bytes": 232,
    "body_bytes": 232,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00af9e20](../00af9/00af9e20.md)
- [00afd380](../00afd/00afd380.md)
- [00afd444](../00afd/00afd444.md)
- [00b115bc](../00b11/00b115bc.md)
- [00b12714](../00b12/00b12714.md)
- [00b15764](../00b15/00b15764.md)
- [00b1e2cc](../00b1e/00b1e2cc.md)
- [00b4c3b8](../00b4c/00b4c3b8.md)

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00bdb030](../00bdb/00bdb030.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)
- [00bde1c0](../00bde/00bde1c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1309 bytes

~~~c

void FUN_00afa8fc(ulong *param_1,byte *param_2,char *param_3)

{
  size_t sVar1;
  size_t __n;
  void *__dest;
  ulong uVar2;
  
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  if ((*param_2 & 1) == 0) {
    __n = (size_t)(*param_2 >> 1);
    sVar1 = strlen(param_3);
    param_2 = param_2 + 1;
  }
  else {
    __n = *(size_t *)(param_2 + 8);
    sVar1 = strlen(param_3);
    param_2 = *(byte **)(param_2 + 0x10);
  }
  uVar2 = __n + sVar1;
  if (uVar2 < 0xfffffffffffffff0) {
    if (uVar2 < 0x17) {
      __dest = (void *)((long)param_1 + 1);
      *(char *)param_1 = (char)((int)__n << 1);
                    /* try { // try from 00afa97c to 00bfa983 has its CatchHandler @ 00aff530 */
    }
    else {
      uVar2 = uVar2 + 0x10 & 0xfffffffffffffff0;
      __dest = (void *)_Znwm(uVar2);
      param_1[1] = __n;
      param_1[2] = (ulong)__dest;
      *param_1 = uVar2 | 1;
    }
    if (__n != 0) {
                    /* try { // try from 00afa9ac to 00bfa9bf has its CatchHandler @ 00aff520 */
      memcpy(__dest,param_2,__n);
    }
    *(undefined1 *)((long)__dest + __n) = 0;
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
              (param_1,param_3,sVar1);
    return;
  }
                    /* WARNING: Subroutine does not return */
  abort();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afa8fc"></a> `00afa8fc` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00afa900"></a> `00afa900` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afa904"></a> `00afa904` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afa908"></a> `00afa908` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afa90c"></a> `00afa90c` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afa910"></a> `00afa910` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00afa914"></a> `00afa914` | `1f 7d 00 a9` | stp xzr,xzr,[x8] | `FALL_THROUGH`
<a id="insn-00afa918"></a> `00afa918` | `1f 09 00 f9` | str xzr,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00afa91c"></a> `00afa91c` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00afa920"></a> `00afa920` | `08 00 40 39` | ldrb w8,[x0] | `FALL_THROUGH`
<a id="insn-00afa924"></a> `00afa924` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00afa928"></a> `00afa928` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00afa92c"></a> `00afa92c` | `e8 00 00 37` | tbnz w8,#0x0,0x00afa948 | `CONDITIONAL_JUMP`
<a id="insn-00afa930"></a> `00afa930` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afa934"></a> `00afa934` | `15 fd 41 d3` | lsr x21,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afa938"></a> `00afa938` | `d6 81 03 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00afa93c"></a> `00afa93c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00afa940"></a> `00afa940` | `f7 06 00 91` | add x23,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00afa944"></a> `00afa944` | `06 00 00 14` | b 0x00afa95c | `UNCONDITIONAL_JUMP`
<a id="insn-00afa948"></a> `00afa948` | `f5 06 40 f9` | ldr x21,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00afa94c"></a> `00afa94c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afa950"></a> `00afa950` | `d0 81 03 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00afa954"></a> `00afa954` | `f7 0a 40 f9` | ldr x23,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00afa958"></a> `00afa958` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00afa95c"></a> `00afa95c` | `a8 02 16 8b` | add x8,x21,x22 | `FALL_THROUGH`
<a id="insn-00afa960"></a> `00afa960` | `1f 41 00 b1` | cmn x8,#0x10 | `FALL_THROUGH`
<a id="insn-00afa964"></a> `00afa964` | `e2 03 00 54` | b.cs 0x00afa9e0 | `CONDITIONAL_JUMP`
<a id="insn-00afa968"></a> `00afa968` | `1f 59 00 f1` | cmp x8,#0x16 | `FALL_THROUGH`
<a id="insn-00afa96c"></a> `00afa96c` | `c8 00 00 54` | b.hi 0x00afa984 | `CONDITIONAL_JUMP`
<a id="insn-00afa970"></a> `00afa970` | `a8 7a 1f 53` | lsl w8,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00afa974"></a> `00afa974` | `f8 03 13 aa` | mov x24,x19 | `FALL_THROUGH`
<a id="insn-00afa978"></a> `00afa978` | `08 17 00 38` | strb w8,[x24], #0x1 | `FALL_THROUGH`
<a id="insn-00afa97c"></a> `00afa97c` | `75 01 00 b5` | cbnz x21,0x00afa9a8 | `CONDITIONAL_JUMP`
<a id="insn-00afa980"></a> `00afa980` | `0e 00 00 14` | b 0x00afa9b8 | `UNCONDITIONAL_JUMP`
<a id="insn-00afa984"></a> `00afa984` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00afa988"></a> `00afa988` | `19 ed 7c 92` | and x25,x8,#-0x10 | `FALL_THROUGH`
<a id="insn-00afa98c"></a> `00afa98c` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00afa990"></a> `00afa990` | `6c 81 03 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00afa994"></a> `00afa994` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00afa998"></a> `00afa998` | `28 03 40 b2` | orr x8,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00afa99c"></a> `00afa99c` | `75 82 00 a9` | stp x21,x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00afa9a0"></a> `00afa9a0` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00afa9a4"></a> `00afa9a4` | `b5 00 00 b4` | cbz x21,0x00afa9b8 | `CONDITIONAL_JUMP`
<a id="insn-00afa9a8"></a> `00afa9a8` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00afa9ac"></a> `00afa9ac` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00afa9b0"></a> `00afa9b0` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00afa9b4"></a> `00afa9b4` | `bf 81 03 94` | bl 0x00bdb0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00afa9b8"></a> `00afa9b8` | `1f 6b 35 38` | strb wzr,[x24, x21, LSL ] | `FALL_THROUGH`
<a id="insn-00afa9bc"></a> `00afa9bc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afa9c0"></a> `00afa9c0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00afa9c4"></a> `00afa9c4` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00afa9c8"></a> `00afa9c8` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afa9cc"></a> `00afa9cc` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afa9d0"></a> `00afa9d0` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afa9d4"></a> `00afa9d4` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afa9d8"></a> `00afa9d8` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00afa9dc"></a> `00afa9dc` | `95 81 03 14` | b 0x00bdb030 | `CALL_TERMINATOR`
<a id="insn-00afa9e0"></a> `00afa9e0` | `f8 8d 03 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afa8fc`](#insn-00afa8fc) 範囲 `[['00afa8fc', '00afa92f']]`
  - `CONDITIONAL_JUMP` [`00afa92c`](#insn-00afa92c) → [`00afa948`](#insn-00afa948)
  - `FALL_THROUGH` [`00afa92c`](#insn-00afa92c) → [`00afa930`](#insn-00afa930)
- ブロック [`00afa930`](#insn-00afa930) 範囲 `[['00afa930', '00afa947']]`
  - `UNCONDITIONAL_JUMP` [`00afa944`](#insn-00afa944) → [`00afa95c`](#insn-00afa95c)
- ブロック [`00afa948`](#insn-00afa948) 範囲 `[['00afa948', '00afa95b']]`
  - `FALL_THROUGH` [`00afa958`](#insn-00afa958) → [`00afa95c`](#insn-00afa95c)
- ブロック [`00afa95c`](#insn-00afa95c) 範囲 `[['00afa95c', '00afa967']]`
  - `CONDITIONAL_JUMP` [`00afa964`](#insn-00afa964) → [`00afa9e0`](#insn-00afa9e0)
  - `FALL_THROUGH` [`00afa964`](#insn-00afa964) → [`00afa968`](#insn-00afa968)
- ブロック [`00afa968`](#insn-00afa968) 範囲 `[['00afa968', '00afa96f']]`
  - `CONDITIONAL_JUMP` [`00afa96c`](#insn-00afa96c) → [`00afa984`](#insn-00afa984)
  - `FALL_THROUGH` [`00afa96c`](#insn-00afa96c) → [`00afa970`](#insn-00afa970)
- ブロック [`00afa970`](#insn-00afa970) 範囲 `[['00afa970', '00afa97b']]`
  - `FALL_THROUGH` [`00afa978`](#insn-00afa978) → [`00afa97c`](#insn-00afa97c)
- ブロック [`00afa97c`](#insn-00afa97c) 範囲 `[['00afa97c', '00afa97f']]`
  - `CONDITIONAL_JUMP` [`00afa97c`](#insn-00afa97c) → [`00afa9a8`](#insn-00afa9a8)
  - `FALL_THROUGH` [`00afa97c`](#insn-00afa97c) → [`00afa980`](#insn-00afa980)
- ブロック [`00afa980`](#insn-00afa980) 範囲 `[['00afa980', '00afa983']]`
  - `UNCONDITIONAL_JUMP` [`00afa980`](#insn-00afa980) → [`00afa9b8`](#insn-00afa9b8)
- ブロック [`00afa984`](#insn-00afa984) 範囲 `[['00afa984', '00afa9a7']]`
  - `CONDITIONAL_JUMP` [`00afa9a4`](#insn-00afa9a4) → [`00afa9b8`](#insn-00afa9b8)
  - `FALL_THROUGH` [`00afa9a4`](#insn-00afa9a4) → [`00afa9a8`](#insn-00afa9a8)
- ブロック [`00afa9a8`](#insn-00afa9a8) 範囲 `[['00afa9a8', '00afa9ab']]`
  - `FALL_THROUGH` [`00afa9a8`](#insn-00afa9a8) → [`00afa9ac`](#insn-00afa9ac)
- ブロック [`00afa9ac`](#insn-00afa9ac) 範囲 `[['00afa9ac', '00afa9b7']]`
  - `FALL_THROUGH` [`00afa9b4`](#insn-00afa9b4) → [`00afa9b8`](#insn-00afa9b8)
- ブロック [`00afa9b8`](#insn-00afa9b8) 範囲 `[['00afa9b8', '00afa9df']]`
- ブロック [`00afa9e0`](#insn-00afa9e0) 範囲 `[['00afa9e0', '00afa9e3']]`

## 命令位置別の参照

- [`00afa8fc`](#insn-00afa8fc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa900`](#insn-00afa900) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa904`](#insn-00afa904) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa908`](#insn-00afa908) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa90c`](#insn-00afa90c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa92c`](#insn-00afa92c) → [`00afa948`](#insn-00afa948) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa938`](#insn-00afa938) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00afa944`](#insn-00afa944) → [`00afa95c`](#insn-00afa95c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa950`](#insn-00afa950) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00afa964`](#insn-00afa964) → [`00afa9e0`](#insn-00afa9e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa96c`](#insn-00afa96c) → [`00afa984`](#insn-00afa984) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa97c`](#insn-00afa97c) → [`00afa9a8`](#insn-00afa9a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa980`](#insn-00afa980) → [`00afa9b8`](#insn-00afa9b8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa990`](#insn-00afa990) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00afa9a4`](#insn-00afa9a4) → [`00afa9b8`](#insn-00afa9b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa9b4`](#insn-00afa9b4) → [`00bdb0b0`](../00bdb/00bdb0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0b0` · 推定シンボル `None` · 推定型 `None`
- [`00afa9c8`](#insn-00afa9c8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa9cc`](#insn-00afa9cc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa9d0`](#insn-00afa9d0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa9d4`](#insn-00afa9d4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa9dc`](#insn-00afa9dc) → [`00bdb030`](../00bdb/00bdb030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb030` · 推定シンボル `None` · 推定型 `None`
- [`00afa9e0`](#insn-00afa9e0) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afa8fc`](#insn-00afa8fc)

~~~json
{
  "source": "00afa8fc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa900`](#insn-00afa900)

~~~json
{
  "source": "00afa900",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa904`](#insn-00afa904)

~~~json
{
  "source": "00afa904",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa908`](#insn-00afa908)

~~~json
{
  "source": "00afa908",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa90c`](#insn-00afa90c)

~~~json
{
  "source": "00afa90c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa92c`](#insn-00afa92c)

~~~json
{
  "source": "00afa92c",
  "target": "00afa948",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa938`](#insn-00afa938)

~~~json
{
  "source": "00afa938",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afa944`](#insn-00afa944)

~~~json
{
  "source": "00afa944",
  "target": "00afa95c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa950`](#insn-00afa950)

~~~json
{
  "source": "00afa950",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afa964`](#insn-00afa964)

~~~json
{
  "source": "00afa964",
  "target": "00afa9e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa96c`](#insn-00afa96c)

~~~json
{
  "source": "00afa96c",
  "target": "00afa984",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa97c`](#insn-00afa97c)

~~~json
{
  "source": "00afa97c",
  "target": "00afa9a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa980`](#insn-00afa980)

~~~json
{
  "source": "00afa980",
  "target": "00afa9b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa990`](#insn-00afa990)

~~~json
{
  "source": "00afa990",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afa9a4`](#insn-00afa9a4)

~~~json
{
  "source": "00afa9a4",
  "target": "00afa9b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa9b4`](#insn-00afa9b4)

~~~json
{
  "source": "00afa9b4",
  "target": "00bdb0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afa9c8`](#insn-00afa9c8)

~~~json
{
  "source": "00afa9c8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa9cc`](#insn-00afa9cc)

~~~json
{
  "source": "00afa9cc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa9d0`](#insn-00afa9d0)

~~~json
{
  "source": "00afa9d0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa9d4`](#insn-00afa9d4)

~~~json
{
  "source": "00afa9d4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa9dc`](#insn-00afa9dc)

~~~json
{
  "source": "00afa9dc",
  "target": "00bdb030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afa9e0`](#insn-00afa9e0)

~~~json
{
  "source": "00afa9e0",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
