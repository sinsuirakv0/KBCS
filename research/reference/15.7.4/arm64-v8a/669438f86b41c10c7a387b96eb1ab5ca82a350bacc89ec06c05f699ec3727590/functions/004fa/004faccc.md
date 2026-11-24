# 004faccc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `004faccc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004faccc.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0012.md#compare-653e73168383d26fb2afc0798ff7e956)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `0051db64`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051d/0051db64.md) · 移動量 `+0x22e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0012.md#compare-ff9097b491075d98dc2b629312bf0992)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004faccc",
  "name": "_ZNK5Botan14Cert_Extension14CRL_ReasonCode12encode_innerEv",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "487445174efcd949d817489a5313a7e55c4141164220791518c63c7eb1e5bd23",
  "source_text_sha256": "487445174efcd949d817489a5313a7e55c4141164220791518c63c7eb1e5bd23",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004faccc",
        "004fadef"
      ],
      [
        "004fae2c",
        "004fae2f"
      ]
    ],
    "bytes_sha256": "828050ef677d427d0bc8b0b201b6739adef3d1991fef11e815155927b1e3b41f",
    "instruction_count": 74,
    "instruction_bytes": 296,
    "body_bytes": 296,
    "indirect": 2,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00483ed8](../00483/00483ed8.md)
- [00512ca8](../00512/00512ca8.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb810](../00bdb/00bdb810.md)
- [00bdbad0](../00bdb/00bdbad0.md)
- [00bdbcc0](../00bdb/00bdbcc0.md)
- [010a5058](../010a5/010a5058.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1492 bytes

~~~c

void _ZNK5Botan14Cert_Extension14CRL_ReasonCode12encode_innerEv(undefined8 param_1,long param_2)

{
  long lVar1;
  void *pvVar2;
  void *pvVar3;
  void *local_a0;
  void *pvStack_98;
  long local_90;
  void *pvStack_88;
  void *local_80;
  undefined8 auStack_78 [2];
  void *local_68;
  void *local_60;
  long local_58;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  pvStack_88 = (void *)0x0;
  local_90 = 0;
  auStack_78[0] = 0;
  local_80 = (void *)0x0;
  pvStack_98 = (void *)0x0;
  local_a0 = (void *)0x0;
  _ZN5Botan6BigIntC1Em(&local_68,*(undefined4 *)(param_2 + 8));
  _ZN5Botan11DER_Encoder6encodeERKNS_6BigIntENS_8ASN1_TagES4_(&local_a0,&local_68,10,0);
  if (local_68 != (void *)0x0) {
    local_60 = local_68;
    (*(code *)PTR_memset_00bea778)(local_68,0,local_58 - (long)local_68);
    free(local_68);
  }
  FUN_00483ed8(param_1,&local_a0);
  pvVar3 = pvStack_88;
  pvVar2 = local_80;
  if (pvStack_88 != (void *)0x0) {
    while (pvVar2 != pvVar3) {
      FUN_00512ca8(auStack_78,(void *)((long)pvVar2 + -0x38));
      pvVar2 = (void *)((long)pvVar2 + -0x38);
    }
    local_80 = pvVar3;
    _ZdlPv(pvStack_88);
  }
  pvVar2 = local_a0;
  if (local_a0 != (void *)0x0) {
    pvStack_98 = local_a0;
    (*(code *)PTR_memset_00bea778)(local_a0,0,local_90 - (long)local_a0);
    free(pvVar2);
  }
  if (*(long *)(lVar1 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004faccc"></a> `004faccc` | `ff 83 02 d1` | sub sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-004facd0"></a> `004facd0` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004facd4"></a> `004facd4` | `f7 3b 00 f9` | str x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004facd8"></a> `004facd8` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004facdc"></a> `004facdc` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004face0"></a> `004face0` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-004face4"></a> `004face4` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004face8"></a> `004face8` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-004facec"></a> `004facec` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-004facf0"></a> `004facf0` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-004facf4"></a> `004facf4` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004facf8"></a> `004facf8` | `01 08 40 b9` | ldr w1,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-004facfc"></a> `004facfc` | `e0 83 00 ad` | stp q0,q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004fad00"></a> `004fad00` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-004fad04"></a> `004fad04` | `a0 a3 00 d1` | sub x0,x29,#0x28 | `FALL_THROUGH`
<a id="insn-004fad08"></a> `004fad08` | `72 83 1b 94` | bl 0x00bdbad0 | `UNCONDITIONAL_CALL`
<a id="insn-004fad0c"></a> `004fad0c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004fad10"></a> `004fad10` | `a1 a3 00 d1` | sub x1,x29,#0x28 | `FALL_THROUGH`
<a id="insn-004fad14"></a> `004fad14` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-004fad18"></a> `004fad18` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-004fad1c"></a> `004fad1c` | `e9 83 1b 94` | bl 0x00bdbcc0 | `UNCONDITIONAL_CALL`
<a id="insn-004fad20"></a> `004fad20` | `b4 83 5d f8` | ldur x20,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004fad24"></a> `004fad24` | `96 37 00 90` | adrp x22,0xbea000 | `FALL_THROUGH`
<a id="insn-004fad28"></a> `004fad28` | `54 01 00 b4` | cbz x20,0x004fad50 | `CONDITIONAL_JUMP`
<a id="insn-004fad2c"></a> `004fad2c` | `b4 03 1e f8` | stur x20,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-004fad30"></a> `004fad30` | `a8 83 5e f8` | ldur x8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-004fad34"></a> `004fad34` | `c9 be 43 f9` | ldr x9,[x22, #0x778] | `FALL_THROUGH`
<a id="insn-004fad38"></a> `004fad38` | `02 01 14 cb` | sub x2,x8,x20 | `FALL_THROUGH`
<a id="insn-004fad3c"></a> `004fad3c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004fad40"></a> `004fad40` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004fad44"></a> `004fad44` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004fad48"></a> `004fad48` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004fad4c"></a> `004fad4c` | `b1 82 1b 94` | bl 0x00bdb810 | `UNCONDITIONAL_CALL`
<a id="insn-004fad50"></a> `004fad50` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004fad54"></a> `004fad54` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-004fad58"></a> `004fad58` | `60 24 fe 97` | bl 0x00483ed8 | `UNCONDITIONAL_CALL`
<a id="insn-004fad5c"></a> `004fad5c` | `f4 0f 40 f9` | ldr x20,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004fad60"></a> `004fad60` | `f4 01 00 b4` | cbz x20,0x004fad9c | `CONDITIONAL_JUMP`
<a id="insn-004fad64"></a> `004fad64` | `f3 13 40 f9` | ldr x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004fad68"></a> `004fad68` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004fad6c"></a> `004fad6c` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-004fad70"></a> `004fad70` | `20 01 00 54` | b.eq 0x004fad94 | `CONDITIONAL_JUMP`
<a id="insn-004fad74"></a> `004fad74` | `f7 03 00 91` | mov x23,sp | `FALL_THROUGH`
<a id="insn-004fad78"></a> `004fad78` | `73 e2 00 d1` | sub x19,x19,#0x38 | `FALL_THROUGH`
<a id="insn-004fad7c"></a> `004fad7c` | `e0 a2 00 91` | add x0,x23,#0x28 | `FALL_THROUGH`
<a id="insn-004fad80"></a> `004fad80` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-004fad84"></a> `004fad84` | `c9 5f 00 94` | bl 0x00512ca8 | `UNCONDITIONAL_CALL`
<a id="insn-004fad88"></a> `004fad88` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-004fad8c"></a> `004fad8c` | `61 ff ff 54` | b.ne 0x004fad78 | `CONDITIONAL_JUMP`
<a id="insn-004fad90"></a> `004fad90` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004fad94"></a> `004fad94` | `f4 13 00 f9` | str x20,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004fad98"></a> `004fad98` | `b2 80 1b 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-004fad9c"></a> `004fad9c` | `f3 03 40 f9` | ldr x19,[sp] | `FALL_THROUGH`
<a id="insn-004fada0"></a> `004fada0` | `53 01 00 b4` | cbz x19,0x004fadc8 | `CONDITIONAL_JUMP`
<a id="insn-004fada4"></a> `004fada4` | `f3 07 00 f9` | str x19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004fada8"></a> `004fada8` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004fadac"></a> `004fadac` | `c9 be 43 f9` | ldr x9,[x22, #0x778] | `FALL_THROUGH`
<a id="insn-004fadb0"></a> `004fadb0` | `02 01 13 cb` | sub x2,x8,x19 | `FALL_THROUGH`
<a id="insn-004fadb4"></a> `004fadb4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004fadb8"></a> `004fadb8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004fadbc"></a> `004fadbc` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004fadc0"></a> `004fadc0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004fadc4"></a> `004fadc4` | `93 82 1b 94` | bl 0x00bdb810 | `UNCONDITIONAL_CALL`
<a id="insn-004fadc8"></a> `004fadc8` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-004fadcc"></a> `004fadcc` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004fadd0"></a> `004fadd0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004fadd4"></a> `004fadd4` | `c1 02 00 54` | b.ne 0x004fae2c | `CONDITIONAL_JUMP`
<a id="insn-004fadd8"></a> `004fadd8` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004faddc"></a> `004faddc` | `f7 3b 40 f9` | ldr x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004fade0"></a> `004fade0` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004fade4"></a> `004fade4` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004fade8"></a> `004fade8` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-004fadec"></a> `004fadec` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004fae2c"></a> `004fae2c` | `99 80 1b 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004faccc`](#insn-004faccc) 範囲 `[['004faccc', '004fad2b']]`
  - `CONDITIONAL_JUMP` [`004fad28`](#insn-004fad28) → [`004fad50`](#insn-004fad50)
  - `FALL_THROUGH` [`004fad28`](#insn-004fad28) → [`004fad2c`](#insn-004fad2c)
- ブロック [`004fad2c`](#insn-004fad2c) 範囲 `[['004fad2c', '004fad4f']]`
  - `FALL_THROUGH` [`004fad4c`](#insn-004fad4c) → [`004fad50`](#insn-004fad50)
- ブロック [`004fad50`](#insn-004fad50) 範囲 `[['004fad50', '004fad63']]`
  - `CONDITIONAL_JUMP` [`004fad60`](#insn-004fad60) → [`004fad9c`](#insn-004fad9c)
  - `FALL_THROUGH` [`004fad60`](#insn-004fad60) → [`004fad64`](#insn-004fad64)
- ブロック [`004fad64`](#insn-004fad64) 範囲 `[['004fad64', '004fad73']]`
  - `CONDITIONAL_JUMP` [`004fad70`](#insn-004fad70) → [`004fad94`](#insn-004fad94)
  - `FALL_THROUGH` [`004fad70`](#insn-004fad70) → [`004fad74`](#insn-004fad74)
- ブロック [`004fad74`](#insn-004fad74) 範囲 `[['004fad74', '004fad77']]`
  - `FALL_THROUGH` [`004fad74`](#insn-004fad74) → [`004fad78`](#insn-004fad78)
- ブロック [`004fad78`](#insn-004fad78) 範囲 `[['004fad78', '004fad8f']]`
  - `CONDITIONAL_JUMP` [`004fad8c`](#insn-004fad8c) → [`004fad78`](#insn-004fad78)
  - `FALL_THROUGH` [`004fad8c`](#insn-004fad8c) → [`004fad90`](#insn-004fad90)
- ブロック [`004fad90`](#insn-004fad90) 範囲 `[['004fad90', '004fad93']]`
  - `FALL_THROUGH` [`004fad90`](#insn-004fad90) → [`004fad94`](#insn-004fad94)
- ブロック [`004fad94`](#insn-004fad94) 範囲 `[['004fad94', '004fad9b']]`
  - `FALL_THROUGH` [`004fad98`](#insn-004fad98) → [`004fad9c`](#insn-004fad9c)
- ブロック [`004fad9c`](#insn-004fad9c) 範囲 `[['004fad9c', '004fada3']]`
  - `CONDITIONAL_JUMP` [`004fada0`](#insn-004fada0) → [`004fadc8`](#insn-004fadc8)
  - `FALL_THROUGH` [`004fada0`](#insn-004fada0) → [`004fada4`](#insn-004fada4)
- ブロック [`004fada4`](#insn-004fada4) 範囲 `[['004fada4', '004fadc7']]`
  - `FALL_THROUGH` [`004fadc4`](#insn-004fadc4) → [`004fadc8`](#insn-004fadc8)
- ブロック [`004fadc8`](#insn-004fadc8) 範囲 `[['004fadc8', '004fadd7']]`
  - `CONDITIONAL_JUMP` [`004fadd4`](#insn-004fadd4) → [`004fae2c`](#insn-004fae2c)
  - `FALL_THROUGH` [`004fadd4`](#insn-004fadd4) → [`004fadd8`](#insn-004fadd8)
- ブロック [`004fadd8`](#insn-004fadd8) 範囲 `[['004fadd8', '004fadef']]`
- ブロック [`004fae2c`](#insn-004fae2c) 範囲 `[['004fae2c', '004fae2f']]`

## 命令位置別の参照

- [`004facd0`](#insn-004facd0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004facd4`](#insn-004facd4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004facd8`](#insn-004facd8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004facdc`](#insn-004facdc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004facf4`](#insn-004facf4) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004facfc`](#insn-004facfc) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad00`](#insn-004fad00) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad08`](#insn-004fad08) → [`00bdbad0`](../00bdb/00bdbad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdbad0` · 推定シンボル `None` · 推定型 `None`
- [`004fad1c`](#insn-004fad1c) → [`00bdbcc0`](../00bdb/00bdbcc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdbcc0` · 推定シンボル `None` · 推定型 `None`
- [`004fad20`](#insn-004fad20) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad28`](#insn-004fad28) → [`004fad50`](#insn-004fad50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad2c`](#insn-004fad2c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad30`](#insn-004fad30) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad34`](#insn-004fad34) → `00bea778`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fad44`](#insn-004fad44) → [`010a5058`](../010a5/010a5058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `010a5058` · 推定シンボル `None` · 推定型 `None`
- [`004fad4c`](#insn-004fad4c) → [`00bdb810`](../00bdb/00bdb810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb810` · 推定シンボル `None` · 推定型 `None`
- [`004fad58`](#insn-004fad58) → [`00483ed8`](../00483/00483ed8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00483ed8` · 推定シンボル `None` · 推定型 `None`
- [`004fad5c`](#insn-004fad5c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad60`](#insn-004fad60) → [`004fad9c`](#insn-004fad9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad64`](#insn-004fad64) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad70`](#insn-004fad70) → [`004fad94`](#insn-004fad94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad84`](#insn-004fad84) → [`00512ca8`](../00512/00512ca8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00512ca8` · 推定シンボル `None` · 推定型 `None`
- [`004fad8c`](#insn-004fad8c) → [`004fad78`](#insn-004fad78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad90`](#insn-004fad90) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad94`](#insn-004fad94) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad98`](#insn-004fad98) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`004fad9c`](#insn-004fad9c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fada0`](#insn-004fada0) → [`004fadc8`](#insn-004fadc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fada4`](#insn-004fada4) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fada8`](#insn-004fada8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fadac`](#insn-004fadac) → `00bea778`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fadbc`](#insn-004fadbc) → [`010a5058`](../010a5/010a5058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `010a5058` · 推定シンボル `None` · 推定型 `None`
- [`004fadc4`](#insn-004fadc4) → [`00bdb810`](../00bdb/00bdb810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb810` · 推定シンボル `None` · 推定型 `None`
- [`004fadcc`](#insn-004fadcc) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fadd4`](#insn-004fadd4) → [`004fae2c`](#insn-004fae2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fadd8`](#insn-004fadd8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004faddc`](#insn-004faddc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fade0`](#insn-004fade0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fade4`](#insn-004fade4) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fae2c`](#insn-004fae2c) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004facd0`](#insn-004facd0)

~~~json
{
  "source": "004facd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004facd4`](#insn-004facd4)

~~~json
{
  "source": "004facd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004facd8`](#insn-004facd8)

~~~json
{
  "source": "004facd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004facdc`](#insn-004facdc)

~~~json
{
  "source": "004facdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004facf4`](#insn-004facf4)

~~~json
{
  "source": "004facf4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004facfc`](#insn-004facfc)

~~~json
{
  "source": "004facfc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad00`](#insn-004fad00)

~~~json
{
  "source": "004fad00",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad08`](#insn-004fad08)

~~~json
{
  "source": "004fad08",
  "target": "00bdbad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fad1c`](#insn-004fad1c)

~~~json
{
  "source": "004fad1c",
  "target": "00bdbcc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fad20`](#insn-004fad20)

~~~json
{
  "source": "004fad20",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad28`](#insn-004fad28)

~~~json
{
  "source": "004fad28",
  "target": "004fad50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad2c`](#insn-004fad2c)

~~~json
{
  "source": "004fad2c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad30`](#insn-004fad30)

~~~json
{
  "source": "004fad30",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad34`](#insn-004fad34)

~~~json
{
  "source": "004fad34",
  "target": "00bea778",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00bea778",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fad44`](#insn-004fad44)

~~~json
{
  "source": "004fad44",
  "target": "010a5058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fad4c`](#insn-004fad4c)

~~~json
{
  "source": "004fad4c",
  "target": "00bdb810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fad58`](#insn-004fad58)

~~~json
{
  "source": "004fad58",
  "target": "00483ed8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fad5c`](#insn-004fad5c)

~~~json
{
  "source": "004fad5c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad60`](#insn-004fad60)

~~~json
{
  "source": "004fad60",
  "target": "004fad9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad64`](#insn-004fad64)

~~~json
{
  "source": "004fad64",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad70`](#insn-004fad70)

~~~json
{
  "source": "004fad70",
  "target": "004fad94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad84`](#insn-004fad84)

~~~json
{
  "source": "004fad84",
  "target": "00512ca8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fad8c`](#insn-004fad8c)

~~~json
{
  "source": "004fad8c",
  "target": "004fad78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad90`](#insn-004fad90)

~~~json
{
  "source": "004fad90",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad94`](#insn-004fad94)

~~~json
{
  "source": "004fad94",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad98`](#insn-004fad98)

~~~json
{
  "source": "004fad98",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fad9c`](#insn-004fad9c)

~~~json
{
  "source": "004fad9c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fada0`](#insn-004fada0)

~~~json
{
  "source": "004fada0",
  "target": "004fadc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fada4`](#insn-004fada4)

~~~json
{
  "source": "004fada4",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fada8`](#insn-004fada8)

~~~json
{
  "source": "004fada8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fadac`](#insn-004fadac)

~~~json
{
  "source": "004fadac",
  "target": "00bea778",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00bea778",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fadbc`](#insn-004fadbc)

~~~json
{
  "source": "004fadbc",
  "target": "010a5058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fadc4`](#insn-004fadc4)

~~~json
{
  "source": "004fadc4",
  "target": "00bdb810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fadcc`](#insn-004fadcc)

~~~json
{
  "source": "004fadcc",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fadd4`](#insn-004fadd4)

~~~json
{
  "source": "004fadd4",
  "target": "004fae2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fadd8`](#insn-004fadd8)

~~~json
{
  "source": "004fadd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004faddc`](#insn-004faddc)

~~~json
{
  "source": "004faddc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fade0`](#insn-004fade0)

~~~json
{
  "source": "004fade0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fade4`](#insn-004fade4)

~~~json
{
  "source": "004fade4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fae2c`](#insn-004fae2c)

~~~json
{
  "source": "004fae2c",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
