# 00bbd0cc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbd194`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd194.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0006.md#compare-ff1d7b122ed2dbac518d0d7e8cc688ca)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbd0cc",
  "name": "FUN_00bbd0cc",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2a283425c7cd0cf6aba397b7283ff5914b400dd9000136bc9e93fcac4f35a085",
  "source_text_sha256": "2a283425c7cd0cf6aba397b7283ff5914b400dd9000136bc9e93fcac4f35a085",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbd0cc",
        "00bbd19b"
      ]
    ],
    "bytes_sha256": "6b22158b87a857638d960eb616f2e3441fbf81a696107e97f0bc3101cde43702",
    "instruction_count": 52,
    "instruction_bytes": 208,
    "body_bytes": 208,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb710](../00bdb/00bdb710.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2342 bytes

~~~c

void FUN_00bbd0cc(long param_1)

{
  undefined8 *puVar1;
  undefined8 *__ptr;
  undefined8 *puVar2;
  
                    /* catch() { ... } // from try @ 00bbbe9c with catch @ 00bbd0dc */
                    /* catch() { ... } // from try @ 00bbbe5c with catch @ 00bbd0e0 */
                    /* catch() { ... } // from try @ 00bbbde0 with catch @ 00bbd0e4 */
  puVar1 = (undefined8 *)(param_1 + 0x330);
  __ptr = *(undefined8 **)(param_1 + 0x1330);
  while (__ptr != (undefined8 *)0x0) {
    while( true ) {
      puVar2 = (undefined8 *)*__ptr;
      *(undefined8 **)(param_1 + 0x1330) = puVar2;
      if (__ptr != puVar1) break;
                    /* catch() { ... } // from try @ 00bbbc48 with catch @ 00bbd10c */
      __ptr = puVar2;
      if (puVar2 == (undefined8 *)0x0) goto LAB_00bbd114;
    }
    free(__ptr);
                    /* catch() { ... } // from try @ 00bbbc58 with catch @ 00bbd0f4 */
    __ptr = *(undefined8 **)(param_1 + 0x1330);
  }
LAB_00bbd114:
  *puVar1 = 0;
  *(undefined8 *)(param_1 + 0x338) = 0;
                    /* catch() { ... } // from try @ 00bbbc3c with catch @ 00bbd120 */
  *(undefined8 **)(param_1 + 0x1330) = puVar1;
                    /* catch() { ... } // from try @ 00bbbbf8 with catch @ 00bbd124 */
                    /* catch() { ... } // from try @ 00bbbaf8 with catch @ 00bbd128 */
  if (*(void **)(param_1 + 0x2d0) != (void *)(param_1 + 0x2e8)) {
    free(*(void **)(param_1 + 0x2d0));
  }
  if (*(void **)(param_1 + 0x298) != (void *)(param_1 + 0x2b0)) {
                    /* catch() { ... } // from try @ 00bbbae8 with catch @ 00bbd140 */
    free(*(void **)(param_1 + 0x298));
  }
  if (*(void **)(param_1 + 0x240) != (void *)(param_1 + 600)) {
                    /* catch() { ... } // from try @ 00bbbadc with catch @ 00bbd154 */
    free(*(void **)(param_1 + 0x240));
  }
                    /* catch() { ... } // from try @ 00bbba94 with catch @ 00bbd158 */
                    /* catch() { ... } // from try @ 00bbb8e4 with catch @ 00bbd15c */
  if (*(void **)(param_1 + 0x128) != (void *)(param_1 + 0x140)) {
    free(*(void **)(param_1 + 0x128));
  }
                    /* catch() { ... } // from try @ 00bbb8d4 with catch @ 00bbd174 */
  if (*(void **)(param_1 + 0x10) != (void *)(param_1 + 0x28)) {
    free(*(void **)(param_1 + 0x10));
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbd0cc"></a> `00bbd0cc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbd0d0"></a> `00bbd0d0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbd0d4"></a> `00bbd0d4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbd0d8"></a> `00bbd0d8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbd0dc"></a> `00bbd0dc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbd0e0"></a> `00bbd0e0` | `00 98 49 f9` | ldr x0,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbd0e4"></a> `00bbd0e4` | `74 c2 0c 91` | add x20,x19,#0x330 | `FALL_THROUGH`
<a id="insn-00bbd0e8"></a> `00bbd0e8` | `a0 00 00 b5` | cbnz x0,0x00bbd0fc | `CONDITIONAL_JUMP`
<a id="insn-00bbd0ec"></a> `00bbd0ec` | `0a 00 00 14` | b 0x00bbd114 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbd0f0"></a> `00bbd0f0` | `88 79 00 94` | bl 0x00bdb710 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd0f4"></a> `00bbd0f4` | `60 9a 49 f9` | ldr x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbd0f8"></a> `00bbd0f8` | `e0 00 00 b4` | cbz x0,0x00bbd114 | `CONDITIONAL_JUMP`
<a id="insn-00bbd0fc"></a> `00bbd0fc` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbd100"></a> `00bbd100` | `1f 00 14 eb` | cmp x0,x20 | `FALL_THROUGH`
<a id="insn-00bbd104"></a> `00bbd104` | `68 9a 09 f9` | str x8,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbd108"></a> `00bbd108` | `41 ff ff 54` | b.ne 0x00bbd0f0 | `CONDITIONAL_JUMP`
<a id="insn-00bbd10c"></a> `00bbd10c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbd110"></a> `00bbd110` | `60 ff ff b5` | cbnz x0,0x00bbd0fc | `CONDITIONAL_JUMP`
<a id="insn-00bbd114"></a> `00bbd114` | `60 6a 41 f9` | ldr x0,[x19, #0x2d0] | `FALL_THROUGH`
<a id="insn-00bbd118"></a> `00bbd118` | `68 a2 0b 91` | add x8,x19,#0x2e8 | `FALL_THROUGH`
<a id="insn-00bbd11c"></a> `00bbd11c` | `9f 7e 00 a9` | stp xzr,xzr,[x20] | `FALL_THROUGH`
<a id="insn-00bbd120"></a> `00bbd120` | `74 9a 09 f9` | str x20,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbd124"></a> `00bbd124` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bbd128"></a> `00bbd128` | `40 00 00 54` | b.eq 0x00bbd130 | `CONDITIONAL_JUMP`
<a id="insn-00bbd12c"></a> `00bbd12c` | `79 79 00 94` | bl 0x00bdb710 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd130"></a> `00bbd130` | `60 4e 41 f9` | ldr x0,[x19, #0x298] | `FALL_THROUGH`
<a id="insn-00bbd134"></a> `00bbd134` | `68 c2 0a 91` | add x8,x19,#0x2b0 | `FALL_THROUGH`
<a id="insn-00bbd138"></a> `00bbd138` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bbd13c"></a> `00bbd13c` | `40 00 00 54` | b.eq 0x00bbd144 | `CONDITIONAL_JUMP`
<a id="insn-00bbd140"></a> `00bbd140` | `74 79 00 94` | bl 0x00bdb710 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd144"></a> `00bbd144` | `60 22 41 f9` | ldr x0,[x19, #0x240] | `FALL_THROUGH`
<a id="insn-00bbd148"></a> `00bbd148` | `68 62 09 91` | add x8,x19,#0x258 | `FALL_THROUGH`
<a id="insn-00bbd14c"></a> `00bbd14c` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bbd150"></a> `00bbd150` | `40 00 00 54` | b.eq 0x00bbd158 | `CONDITIONAL_JUMP`
<a id="insn-00bbd154"></a> `00bbd154` | `6f 79 00 94` | bl 0x00bdb710 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd158"></a> `00bbd158` | `60 96 40 f9` | ldr x0,[x19, #0x128] | `FALL_THROUGH`
<a id="insn-00bbd15c"></a> `00bbd15c` | `68 02 05 91` | add x8,x19,#0x140 | `FALL_THROUGH`
<a id="insn-00bbd160"></a> `00bbd160` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bbd164"></a> `00bbd164` | `40 00 00 54` | b.eq 0x00bbd16c | `CONDITIONAL_JUMP`
<a id="insn-00bbd168"></a> `00bbd168` | `6a 79 00 94` | bl 0x00bdb710 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd16c"></a> `00bbd16c` | `60 0a 40 f9` | ldr x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbd170"></a> `00bbd170` | `68 a2 00 91` | add x8,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00bbd174"></a> `00bbd174` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bbd178"></a> `00bbd178` | `a0 00 00 54` | b.eq 0x00bbd18c | `CONDITIONAL_JUMP`
<a id="insn-00bbd17c"></a> `00bbd17c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbd180"></a> `00bbd180` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbd184"></a> `00bbd184` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbd188"></a> `00bbd188` | `62 79 00 14` | b 0x00bdb710 | `CALL_TERMINATOR`
<a id="insn-00bbd18c"></a> `00bbd18c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbd190"></a> `00bbd190` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbd194"></a> `00bbd194` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbd198"></a> `00bbd198` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbd0cc`](#insn-00bbd0cc) 範囲 `[['00bbd0cc', '00bbd0db']]`
  - `FALL_THROUGH` [`00bbd0d8`](#insn-00bbd0d8) → [`00bbd0dc`](#insn-00bbd0dc)
- ブロック [`00bbd0dc`](#insn-00bbd0dc) 範囲 `[['00bbd0dc', '00bbd0df']]`
  - `FALL_THROUGH` [`00bbd0dc`](#insn-00bbd0dc) → [`00bbd0e0`](#insn-00bbd0e0)
- ブロック [`00bbd0e0`](#insn-00bbd0e0) 範囲 `[['00bbd0e0', '00bbd0e3']]`
  - `FALL_THROUGH` [`00bbd0e0`](#insn-00bbd0e0) → [`00bbd0e4`](#insn-00bbd0e4)
- ブロック [`00bbd0e4`](#insn-00bbd0e4) 範囲 `[['00bbd0e4', '00bbd0eb']]`
  - `CONDITIONAL_JUMP` [`00bbd0e8`](#insn-00bbd0e8) → [`00bbd0fc`](#insn-00bbd0fc)
  - `FALL_THROUGH` [`00bbd0e8`](#insn-00bbd0e8) → [`00bbd0ec`](#insn-00bbd0ec)
- ブロック [`00bbd0ec`](#insn-00bbd0ec) 範囲 `[['00bbd0ec', '00bbd0ef']]`
  - `UNCONDITIONAL_JUMP` [`00bbd0ec`](#insn-00bbd0ec) → [`00bbd114`](#insn-00bbd114)
- ブロック [`00bbd0f0`](#insn-00bbd0f0) 範囲 `[['00bbd0f0', '00bbd0f3']]`
  - `FALL_THROUGH` [`00bbd0f0`](#insn-00bbd0f0) → [`00bbd0f4`](#insn-00bbd0f4)
- ブロック [`00bbd0f4`](#insn-00bbd0f4) 範囲 `[['00bbd0f4', '00bbd0fb']]`
  - `CONDITIONAL_JUMP` [`00bbd0f8`](#insn-00bbd0f8) → [`00bbd114`](#insn-00bbd114)
  - `FALL_THROUGH` [`00bbd0f8`](#insn-00bbd0f8) → [`00bbd0fc`](#insn-00bbd0fc)
- ブロック [`00bbd0fc`](#insn-00bbd0fc) 範囲 `[['00bbd0fc', '00bbd10b']]`
  - `CONDITIONAL_JUMP` [`00bbd108`](#insn-00bbd108) → [`00bbd0f0`](#insn-00bbd0f0)
  - `FALL_THROUGH` [`00bbd108`](#insn-00bbd108) → [`00bbd10c`](#insn-00bbd10c)
- ブロック [`00bbd10c`](#insn-00bbd10c) 範囲 `[['00bbd10c', '00bbd113']]`
  - `CONDITIONAL_JUMP` [`00bbd110`](#insn-00bbd110) → [`00bbd0fc`](#insn-00bbd0fc)
  - `FALL_THROUGH` [`00bbd110`](#insn-00bbd110) → [`00bbd114`](#insn-00bbd114)
- ブロック [`00bbd114`](#insn-00bbd114) 範囲 `[['00bbd114', '00bbd11f']]`
  - `FALL_THROUGH` [`00bbd11c`](#insn-00bbd11c) → [`00bbd120`](#insn-00bbd120)
- ブロック [`00bbd120`](#insn-00bbd120) 範囲 `[['00bbd120', '00bbd123']]`
  - `FALL_THROUGH` [`00bbd120`](#insn-00bbd120) → [`00bbd124`](#insn-00bbd124)
- ブロック [`00bbd124`](#insn-00bbd124) 範囲 `[['00bbd124', '00bbd127']]`
  - `FALL_THROUGH` [`00bbd124`](#insn-00bbd124) → [`00bbd128`](#insn-00bbd128)
- ブロック [`00bbd128`](#insn-00bbd128) 範囲 `[['00bbd128', '00bbd12b']]`
  - `CONDITIONAL_JUMP` [`00bbd128`](#insn-00bbd128) → [`00bbd130`](#insn-00bbd130)
  - `FALL_THROUGH` [`00bbd128`](#insn-00bbd128) → [`00bbd12c`](#insn-00bbd12c)
- ブロック [`00bbd12c`](#insn-00bbd12c) 範囲 `[['00bbd12c', '00bbd12f']]`
  - `FALL_THROUGH` [`00bbd12c`](#insn-00bbd12c) → [`00bbd130`](#insn-00bbd130)
- ブロック [`00bbd130`](#insn-00bbd130) 範囲 `[['00bbd130', '00bbd13f']]`
  - `CONDITIONAL_JUMP` [`00bbd13c`](#insn-00bbd13c) → [`00bbd144`](#insn-00bbd144)
  - `FALL_THROUGH` [`00bbd13c`](#insn-00bbd13c) → [`00bbd140`](#insn-00bbd140)
- ブロック [`00bbd140`](#insn-00bbd140) 範囲 `[['00bbd140', '00bbd143']]`
  - `FALL_THROUGH` [`00bbd140`](#insn-00bbd140) → [`00bbd144`](#insn-00bbd144)
- ブロック [`00bbd144`](#insn-00bbd144) 範囲 `[['00bbd144', '00bbd153']]`
  - `CONDITIONAL_JUMP` [`00bbd150`](#insn-00bbd150) → [`00bbd158`](#insn-00bbd158)
  - `FALL_THROUGH` [`00bbd150`](#insn-00bbd150) → [`00bbd154`](#insn-00bbd154)
- ブロック [`00bbd154`](#insn-00bbd154) 範囲 `[['00bbd154', '00bbd157']]`
  - `FALL_THROUGH` [`00bbd154`](#insn-00bbd154) → [`00bbd158`](#insn-00bbd158)
- ブロック [`00bbd158`](#insn-00bbd158) 範囲 `[['00bbd158', '00bbd15b']]`
  - `FALL_THROUGH` [`00bbd158`](#insn-00bbd158) → [`00bbd15c`](#insn-00bbd15c)
- ブロック [`00bbd15c`](#insn-00bbd15c) 範囲 `[['00bbd15c', '00bbd167']]`
  - `CONDITIONAL_JUMP` [`00bbd164`](#insn-00bbd164) → [`00bbd16c`](#insn-00bbd16c)
  - `FALL_THROUGH` [`00bbd164`](#insn-00bbd164) → [`00bbd168`](#insn-00bbd168)
- ブロック [`00bbd168`](#insn-00bbd168) 範囲 `[['00bbd168', '00bbd16b']]`
  - `FALL_THROUGH` [`00bbd168`](#insn-00bbd168) → [`00bbd16c`](#insn-00bbd16c)
- ブロック [`00bbd16c`](#insn-00bbd16c) 範囲 `[['00bbd16c', '00bbd173']]`
  - `FALL_THROUGH` [`00bbd170`](#insn-00bbd170) → [`00bbd174`](#insn-00bbd174)
- ブロック [`00bbd174`](#insn-00bbd174) 範囲 `[['00bbd174', '00bbd17b']]`
  - `CONDITIONAL_JUMP` [`00bbd178`](#insn-00bbd178) → [`00bbd18c`](#insn-00bbd18c)
  - `FALL_THROUGH` [`00bbd178`](#insn-00bbd178) → [`00bbd17c`](#insn-00bbd17c)
- ブロック [`00bbd17c`](#insn-00bbd17c) 範囲 `[['00bbd17c', '00bbd18b']]`
- ブロック [`00bbd18c`](#insn-00bbd18c) 範囲 `[['00bbd18c', '00bbd19b']]`

## 命令位置別の参照

- [`00bbd0d0`](#insn-00bbd0d0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd0d4`](#insn-00bbd0d4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd0e8`](#insn-00bbd0e8) → [`00bbd0fc`](#insn-00bbd0fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd0ec`](#insn-00bbd0ec) → [`00bbd114`](#insn-00bbd114) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd0f0`](#insn-00bbd0f0) → [`00bdb710`](../00bdb/00bdb710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb710` · 推定シンボル `None` · 推定型 `None`
- [`00bbd0f8`](#insn-00bbd0f8) → [`00bbd114`](#insn-00bbd114) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd108`](#insn-00bbd108) → [`00bbd0f0`](#insn-00bbd0f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd110`](#insn-00bbd110) → [`00bbd0fc`](#insn-00bbd0fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd128`](#insn-00bbd128) → [`00bbd130`](#insn-00bbd130) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd12c`](#insn-00bbd12c) → [`00bdb710`](../00bdb/00bdb710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb710` · 推定シンボル `None` · 推定型 `None`
- [`00bbd13c`](#insn-00bbd13c) → [`00bbd144`](#insn-00bbd144) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd140`](#insn-00bbd140) → [`00bdb710`](../00bdb/00bdb710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb710` · 推定シンボル `None` · 推定型 `None`
- [`00bbd150`](#insn-00bbd150) → [`00bbd158`](#insn-00bbd158) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd154`](#insn-00bbd154) → [`00bdb710`](../00bdb/00bdb710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb710` · 推定シンボル `None` · 推定型 `None`
- [`00bbd164`](#insn-00bbd164) → [`00bbd16c`](#insn-00bbd16c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd168`](#insn-00bbd168) → [`00bdb710`](../00bdb/00bdb710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb710` · 推定シンボル `None` · 推定型 `None`
- [`00bbd178`](#insn-00bbd178) → [`00bbd18c`](#insn-00bbd18c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd17c`](#insn-00bbd17c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd180`](#insn-00bbd180) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd188`](#insn-00bbd188) → [`00bdb710`](../00bdb/00bdb710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb710` · 推定シンボル `None` · 推定型 `None`
- [`00bbd18c`](#insn-00bbd18c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd190`](#insn-00bbd190) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbd0d0`](#insn-00bbd0d0)

~~~json
{
  "source": "00bbd0d0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd0d4`](#insn-00bbd0d4)

~~~json
{
  "source": "00bbd0d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd0e8`](#insn-00bbd0e8)

~~~json
{
  "source": "00bbd0e8",
  "target": "00bbd0fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd0ec`](#insn-00bbd0ec)

~~~json
{
  "source": "00bbd0ec",
  "target": "00bbd114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd0f0`](#insn-00bbd0f0)

~~~json
{
  "source": "00bbd0f0",
  "target": "00bdb710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd0f8`](#insn-00bbd0f8)

~~~json
{
  "source": "00bbd0f8",
  "target": "00bbd114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd108`](#insn-00bbd108)

~~~json
{
  "source": "00bbd108",
  "target": "00bbd0f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd110`](#insn-00bbd110)

~~~json
{
  "source": "00bbd110",
  "target": "00bbd0fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd128`](#insn-00bbd128)

~~~json
{
  "source": "00bbd128",
  "target": "00bbd130",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd12c`](#insn-00bbd12c)

~~~json
{
  "source": "00bbd12c",
  "target": "00bdb710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd13c`](#insn-00bbd13c)

~~~json
{
  "source": "00bbd13c",
  "target": "00bbd144",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd140`](#insn-00bbd140)

~~~json
{
  "source": "00bbd140",
  "target": "00bdb710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd150`](#insn-00bbd150)

~~~json
{
  "source": "00bbd150",
  "target": "00bbd158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd154`](#insn-00bbd154)

~~~json
{
  "source": "00bbd154",
  "target": "00bdb710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd164`](#insn-00bbd164)

~~~json
{
  "source": "00bbd164",
  "target": "00bbd16c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd168`](#insn-00bbd168)

~~~json
{
  "source": "00bbd168",
  "target": "00bdb710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd178`](#insn-00bbd178)

~~~json
{
  "source": "00bbd178",
  "target": "00bbd18c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd17c`](#insn-00bbd17c)

~~~json
{
  "source": "00bbd17c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd180`](#insn-00bbd180)

~~~json
{
  "source": "00bbd180",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd188`](#insn-00bbd188)

~~~json
{
  "source": "00bbd188",
  "target": "00bdb710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd18c`](#insn-00bbd18c)

~~~json
{
  "source": "00bbd18c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd190`](#insn-00bbd190)

~~~json
{
  "source": "00bbd190",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
