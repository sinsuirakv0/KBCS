# 00bbada4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bba97c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba97c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0079.md#compare-37e606e25e7f507f17918b94124832e5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbae40`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbae40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0079.md#compare-27bae1336b980350b9b6b971199fd5ec)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbada4",
  "name": "_ZN8firebase9messaging33SetTokenRegistrationOnInitEnabledEb",
  "size": 320,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d5c6b31e7d262e4b56b923e94305228fdf07f0b619ec44a72b5b09e5ea47ff15",
  "source_text_sha256": "d5c6b31e7d262e4b56b923e94305228fdf07f0b619ec44a72b5b09e5ea47ff15",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbada4",
        "00bbaee3"
      ]
    ],
    "bytes_sha256": "9a7692de9168297c17676c7be80cb5422ce4b9e03de4381430ef6e2124596271",
    "instruction_count": 80,
    "instruction_bytes": 320,
    "body_bytes": 320,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5aae0](../00c5a/00c5aae0.md)

## 呼び出し先

- [00497a48](../00497/00497a48.md)
- [00574cec](../00574/00574cec.md)
- [00bbaf50](../00bba/00bbaf50.md)
- [00c5aca0](../00c5a/00c5aca0.md)
- [00c5b000](../00c5b/00c5b000.md)
- [00c5b080](../00c5b/00c5b080.md)

## 関連文字列（未確認候補）

~~~text
"Messaging not initialized."
"internal::IsInitialized()"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1241 bytes

~~~c

void _ZN8firebase9messaging33SetTokenRegistrationOnInitEnabledEb(uint param_1)

{
  char cVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  
  if (DAT_01126360 == 0) {
    DAT_01126400 = 1;
    if ((param_1 & 1) == 0) {
      DAT_01126400 = 2;
    }
  }
  else {
    uVar2 = _ZNK8firebase3App9GetJNIEnvEv(DAT_01126360);
    if (DAT_01126360 == 0) {
      _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
      _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
      if (DAT_01126360 == 0) {
        FUN_00574cec(uVar2,DAT_01126398,DAT_011262c0,param_1 & 1);
        return;
      }
    }
    uVar3 = _ZNK8firebase3App9GetJNIEnvEv(DAT_01126360);
    cVar1 = FUN_00497a48(uVar3,DAT_01126398,DAT_011262b8);
    FUN_00574cec(uVar2,DAT_01126398,DAT_011262c0,param_1 & 1);
    if (cVar1 != '\0') {
      return;
    }
    if (DAT_01126360 == 0) {
      _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
      _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
      if (DAT_01126360 == 0) goto LAB_00bbae7c;
    }
    uVar2 = _ZNK8firebase3App9GetJNIEnvEv();
    cVar1 = FUN_00497a48(uVar2,DAT_01126398,DAT_011262b8);
    if (cVar1 != '\0') {
LAB_00bbae7c:
      FUN_00bbaf50();
      return;
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbada4"></a> `00bbada4` | `f7 0f 1c f8` | str x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bbada8"></a> `00bbada8` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbadac"></a> `00bbadac` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbadb0"></a> `00bbadb0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbadb4"></a> `00bbadb4` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbadb8"></a> `00bbadb8` | `75 2b 00 90` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbadbc"></a> `00bbadbc` | `a8 b2 41 f9` | ldr x8,[x21, #0x360] | `FALL_THROUGH`
<a id="insn-00bbadc0"></a> `00bbadc0` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bbadc4"></a> `00bbadc4` | `68 06 00 b4` | cbz x8,0x00bbae90 | `CONDITIONAL_JUMP`
<a id="insn-00bbadc8"></a> `00bbadc8` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbadcc"></a> `00bbadcc` | `ad 80 02 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbadd0"></a> `00bbadd0` | `a8 b2 41 f9` | ldr x8,[x21, #0x360] | `FALL_THROUGH`
<a id="insn-00bbadd4"></a> `00bbadd4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbadd8"></a> `00bbadd8` | `28 01 00 b5` | cbnz x8,0x00bbadfc | `CONDITIONAL_JUMP`
<a id="insn-00bbaddc"></a> `00bbaddc` | `40 b7 ff 90` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbade0"></a> `00bbade0` | `00 54 24 91` | add x0,x0,#0x915 | `FALL_THROUGH`
<a id="insn-00bbade4"></a> `00bbade4` | `af 7f 02 94` | bl 0x00c5aca0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbade8"></a> `00bbade8` | `a0 b7 ff d0` | adrp x0,0x2b0000 | `FALL_THROUGH`
<a id="insn-00bbadec"></a> `00bbadec` | `00 dc 1d 91` | add x0,x0,#0x777 | `FALL_THROUGH`
<a id="insn-00bbadf0"></a> `00bbadf0` | `84 80 02 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bbadf4"></a> `00bbadf4` | `a8 b2 41 f9` | ldr x8,[x21, #0x360] | `FALL_THROUGH`
<a id="insn-00bbadf8"></a> `00bbadf8` | `08 06 00 b4` | cbz x8,0x00bbaeb8 | `CONDITIONAL_JUMP`
<a id="insn-00bbadfc"></a> `00bbadfc` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbae00"></a> `00bbae00` | `a0 80 02 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbae04"></a> `00bbae04` | `77 2b 00 90` | adrp x23,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbae08"></a> `00bbae08` | `76 2b 00 90` | adrp x22,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbae0c"></a> `00bbae0c` | `f7 e2 0a 91` | add x23,x23,#0x2b8 | `FALL_THROUGH`
<a id="insn-00bbae10"></a> `00bbae10` | `c1 ce 41 f9` | ldr x1,[x22, #0x398] | `FALL_THROUGH`
<a id="insn-00bbae14"></a> `00bbae14` | `e2 02 40 f9` | ldr x2,[x23] | `FALL_THROUGH`
<a id="insn-00bbae18"></a> `00bbae18` | `0c 73 e3 97` | bl 0x00497a48 | `UNCONDITIONAL_CALL`
<a id="insn-00bbae1c"></a> `00bbae1c` | `c1 ce 41 f9` | ldr x1,[x22, #0x398] | `FALL_THROUGH`
<a id="insn-00bbae20"></a> `00bbae20` | `e2 06 40 f9` | ldr x2,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bbae24"></a> `00bbae24` | `17 1c 00 12` | and w23,w0,#0xff | `FALL_THROUGH`
<a id="insn-00bbae28"></a> `00bbae28` | `63 02 00 12` | and w3,w19,#0x1 | `FALL_THROUGH`
<a id="insn-00bbae2c"></a> `00bbae2c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbae30"></a> `00bbae30` | `af e7 e6 97` | bl 0x00574cec | `UNCONDITIONAL_CALL`
<a id="insn-00bbae34"></a> `00bbae34` | `97 03 00 35` | cbnz w23,0x00bbaea4 | `CONDITIONAL_JUMP`
<a id="insn-00bbae38"></a> `00bbae38` | `a0 b2 41 f9` | ldr x0,[x21, #0x360] | `FALL_THROUGH`
<a id="insn-00bbae3c"></a> `00bbae3c` | `20 01 00 b5` | cbnz x0,0x00bbae60 | `CONDITIONAL_JUMP`
<a id="insn-00bbae40"></a> `00bbae40` | `40 b7 ff 90` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbae44"></a> `00bbae44` | `00 54 24 91` | add x0,x0,#0x915 | `FALL_THROUGH`
<a id="insn-00bbae48"></a> `00bbae48` | `96 7f 02 94` | bl 0x00c5aca0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbae4c"></a> `00bbae4c` | `a0 b7 ff d0` | adrp x0,0x2b0000 | `FALL_THROUGH`
<a id="insn-00bbae50"></a> `00bbae50` | `00 dc 1d 91` | add x0,x0,#0x777 | `FALL_THROUGH`
<a id="insn-00bbae54"></a> `00bbae54` | `6b 80 02 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bbae58"></a> `00bbae58` | `a0 b2 41 f9` | ldr x0,[x21, #0x360] | `FALL_THROUGH`
<a id="insn-00bbae5c"></a> `00bbae5c` | `00 01 00 b4` | cbz x0,0x00bbae7c | `CONDITIONAL_JUMP`
<a id="insn-00bbae60"></a> `00bbae60` | `88 80 02 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbae64"></a> `00bbae64` | `68 2b 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbae68"></a> `00bbae68` | `c1 ce 41 f9` | ldr x1,[x22, #0x398] | `FALL_THROUGH`
<a id="insn-00bbae6c"></a> `00bbae6c` | `02 5d 41 f9` | ldr x2,[x8, #0x2b8] | `FALL_THROUGH`
<a id="insn-00bbae70"></a> `00bbae70` | `f6 72 e3 97` | bl 0x00497a48 | `UNCONDITIONAL_CALL`
<a id="insn-00bbae74"></a> `00bbae74` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bbae78"></a> `00bbae78` | `60 01 00 54` | b.eq 0x00bbaea4 | `CONDITIONAL_JUMP`
<a id="insn-00bbae7c"></a> `00bbae7c` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbae80"></a> `00bbae80` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbae84"></a> `00bbae84` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbae88"></a> `00bbae88` | `f7 07 44 f8` | ldr x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bbae8c"></a> `00bbae8c` | `31 00 00 14` | b 0x00bbaf50 | `CALL_TERMINATOR`
<a id="insn-00bbae90"></a> `00bbae90` | `7f 02 00 72` | tst w19,#0x1 | `FALL_THROUGH`
<a id="insn-00bbae94"></a> `00bbae94` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbae98"></a> `00bbae98` | `08 15 88 1a` | cinc w8,w8,eq | `FALL_THROUGH`
<a id="insn-00bbae9c"></a> `00bbae9c` | `69 2b 00 90` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbaea0"></a> `00bbaea0` | `28 01 04 b9` | str w8,[x9, #0x400] | `FALL_THROUGH`
<a id="insn-00bbaea4"></a> `00bbaea4` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbaea8"></a> `00bbaea8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbaeac"></a> `00bbaeac` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaeb0"></a> `00bbaeb0` | `f7 07 44 f8` | ldr x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bbaeb4"></a> `00bbaeb4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbaeb8"></a> `00bbaeb8` | `68 2b 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbaebc"></a> `00bbaebc` | `69 2b 00 90` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbaec0"></a> `00bbaec0` | `01 cd 41 f9` | ldr x1,[x8, #0x398] | `FALL_THROUGH`
<a id="insn-00bbaec4"></a> `00bbaec4` | `22 61 41 f9` | ldr x2,[x9, #0x2c0] | `FALL_THROUGH`
<a id="insn-00bbaec8"></a> `00bbaec8` | `63 02 00 12` | and w3,w19,#0x1 | `FALL_THROUGH`
<a id="insn-00bbaecc"></a> `00bbaecc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbaed0"></a> `00bbaed0` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbaed4"></a> `00bbaed4` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbaed8"></a> `00bbaed8` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaedc"></a> `00bbaedc` | `f7 07 44 f8` | ldr x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bbaee0"></a> `00bbaee0` | `83 e7 e6 17` | b 0x00574cec | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbada4`](#insn-00bbada4) 範囲 `[['00bbada4', '00bbadc7']]`
  - `CONDITIONAL_JUMP` [`00bbadc4`](#insn-00bbadc4) → [`00bbae90`](#insn-00bbae90)
  - `FALL_THROUGH` [`00bbadc4`](#insn-00bbadc4) → [`00bbadc8`](#insn-00bbadc8)
- ブロック [`00bbadc8`](#insn-00bbadc8) 範囲 `[['00bbadc8', '00bbaddb']]`
  - `CONDITIONAL_JUMP` [`00bbadd8`](#insn-00bbadd8) → [`00bbadfc`](#insn-00bbadfc)
  - `FALL_THROUGH` [`00bbadd8`](#insn-00bbadd8) → [`00bbaddc`](#insn-00bbaddc)
- ブロック [`00bbaddc`](#insn-00bbaddc) 範囲 `[['00bbaddc', '00bbadfb']]`
  - `CONDITIONAL_JUMP` [`00bbadf8`](#insn-00bbadf8) → [`00bbaeb8`](#insn-00bbaeb8)
  - `FALL_THROUGH` [`00bbadf8`](#insn-00bbadf8) → [`00bbadfc`](#insn-00bbadfc)
- ブロック [`00bbadfc`](#insn-00bbadfc) 範囲 `[['00bbadfc', '00bbae37']]`
  - `CONDITIONAL_JUMP` [`00bbae34`](#insn-00bbae34) → [`00bbaea4`](#insn-00bbaea4)
  - `FALL_THROUGH` [`00bbae34`](#insn-00bbae34) → [`00bbae38`](#insn-00bbae38)
- ブロック [`00bbae38`](#insn-00bbae38) 範囲 `[['00bbae38', '00bbae3f']]`
  - `CONDITIONAL_JUMP` [`00bbae3c`](#insn-00bbae3c) → [`00bbae60`](#insn-00bbae60)
  - `FALL_THROUGH` [`00bbae3c`](#insn-00bbae3c) → [`00bbae40`](#insn-00bbae40)
- ブロック [`00bbae40`](#insn-00bbae40) 範囲 `[['00bbae40', '00bbae5f']]`
  - `CONDITIONAL_JUMP` [`00bbae5c`](#insn-00bbae5c) → [`00bbae7c`](#insn-00bbae7c)
  - `FALL_THROUGH` [`00bbae5c`](#insn-00bbae5c) → [`00bbae60`](#insn-00bbae60)
- ブロック [`00bbae60`](#insn-00bbae60) 範囲 `[['00bbae60', '00bbae7b']]`
  - `CONDITIONAL_JUMP` [`00bbae78`](#insn-00bbae78) → [`00bbaea4`](#insn-00bbaea4)
  - `FALL_THROUGH` [`00bbae78`](#insn-00bbae78) → [`00bbae7c`](#insn-00bbae7c)
- ブロック [`00bbae7c`](#insn-00bbae7c) 範囲 `[['00bbae7c', '00bbae8f']]`
- ブロック [`00bbae90`](#insn-00bbae90) 範囲 `[['00bbae90', '00bbaea3']]`
  - `FALL_THROUGH` [`00bbaea0`](#insn-00bbaea0) → [`00bbaea4`](#insn-00bbaea4)
- ブロック [`00bbaea4`](#insn-00bbaea4) 範囲 `[['00bbaea4', '00bbaeb7']]`
- ブロック [`00bbaeb8`](#insn-00bbaeb8) 範囲 `[['00bbaeb8', '00bbaee3']]`

## 命令位置別の参照

- [`00bbada4`](#insn-00bbada4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbada8`](#insn-00bbada8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadac`](#insn-00bbadac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadb0`](#insn-00bbadb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadbc`](#insn-00bbadbc) → `01126360`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbadc4`](#insn-00bbadc4) → [`00bbae90`](#insn-00bbae90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadcc`](#insn-00bbadcc) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bbadd0`](#insn-00bbadd0) → `01126360`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbadd8`](#insn-00bbadd8) → [`00bbadfc`](#insn-00bbadfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbade0`](#insn-00bbade0) → `002a2915`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbade4`](#insn-00bbade4) → [`00c5aca0`](../00c5a/00c5aca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aca0` · 推定シンボル `None` · 推定型 `None`
- [`00bbadec`](#insn-00bbadec) → `002b0777`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbadf0`](#insn-00bbadf0) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bbadf4`](#insn-00bbadf4) → `01126360`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbadf8`](#insn-00bbadf8) → [`00bbaeb8`](#insn-00bbaeb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae00`](#insn-00bbae00) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bbae10`](#insn-00bbae10) → `01126398`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbae14`](#insn-00bbae14) → `011262b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbae18`](#insn-00bbae18) → [`00497a48`](../00497/00497a48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497a48` · 推定シンボル `None` · 推定型 `None`
- [`00bbae1c`](#insn-00bbae1c) → `01126398`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbae20`](#insn-00bbae20) → `011262c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbae30`](#insn-00bbae30) → [`00574cec`](../00574/00574cec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00574cec` · 推定シンボル `None` · 推定型 `None`
- [`00bbae34`](#insn-00bbae34) → [`00bbaea4`](#insn-00bbaea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae38`](#insn-00bbae38) → `01126360`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbae3c`](#insn-00bbae3c) → [`00bbae60`](#insn-00bbae60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae44`](#insn-00bbae44) → `002a2915`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbae48`](#insn-00bbae48) → [`00c5aca0`](../00c5a/00c5aca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aca0` · 推定シンボル `None` · 推定型 `None`
- [`00bbae50`](#insn-00bbae50) → `002b0777`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbae54`](#insn-00bbae54) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bbae58`](#insn-00bbae58) → `01126360`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbae5c`](#insn-00bbae5c) → [`00bbae7c`](#insn-00bbae7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae60`](#insn-00bbae60) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bbae68`](#insn-00bbae68) → `01126398`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbae6c`](#insn-00bbae6c) → `011262b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbae70`](#insn-00bbae70) → [`00497a48`](../00497/00497a48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497a48` · 推定シンボル `None` · 推定型 `None`
- [`00bbae78`](#insn-00bbae78) → [`00bbaea4`](#insn-00bbaea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae7c`](#insn-00bbae7c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae80`](#insn-00bbae80) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae84`](#insn-00bbae84) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae8c`](#insn-00bbae8c) → [`00bbaf50`](00bbaf50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbaf50` · 推定シンボル `None` · 推定型 `None`
- [`00bbaea0`](#insn-00bbaea0) → `01126400`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00bbaea4`](#insn-00bbaea4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaea8`](#insn-00bbaea8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaeac`](#insn-00bbaeac) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaec0`](#insn-00bbaec0) → `01126398`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbaec4`](#insn-00bbaec4) → `011262c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbaed0`](#insn-00bbaed0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaed4`](#insn-00bbaed4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaed8`](#insn-00bbaed8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaee0`](#insn-00bbaee0) → [`00574cec`](../00574/00574cec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00574cec` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbada4`](#insn-00bbada4)

~~~json
{
  "source": "00bbada4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbada8`](#insn-00bbada8)

~~~json
{
  "source": "00bbada8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadac`](#insn-00bbadac)

~~~json
{
  "source": "00bbadac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadb0`](#insn-00bbadb0)

~~~json
{
  "source": "00bbadb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadbc`](#insn-00bbadbc)

~~~json
{
  "source": "00bbadbc",
  "target": "01126360",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126360",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbadc4`](#insn-00bbadc4)

~~~json
{
  "source": "00bbadc4",
  "target": "00bbae90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadcc`](#insn-00bbadcc)

~~~json
{
  "source": "00bbadcc",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbadd0`](#insn-00bbadd0)

~~~json
{
  "source": "00bbadd0",
  "target": "01126360",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126360",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbadd8`](#insn-00bbadd8)

~~~json
{
  "source": "00bbadd8",
  "target": "00bbadfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbade0`](#insn-00bbade0)

~~~json
{
  "source": "00bbade0",
  "target": "002a2915",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2915",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "002a2915",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbade4`](#insn-00bbade4)

~~~json
{
  "source": "00bbade4",
  "target": "00c5aca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbadec`](#insn-00bbadec)

~~~json
{
  "source": "00bbadec",
  "target": "002b0777",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b0777",
  "offset": 0,
  "size": 27,
  "datatype": "string",
  "bytes": "4d6573736167696e67206e6f7420696e697469616c697a65642e00",
  "capture_start": "002b0777",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbadf0`](#insn-00bbadf0)

~~~json
{
  "source": "00bbadf0",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbadf4`](#insn-00bbadf4)

~~~json
{
  "source": "00bbadf4",
  "target": "01126360",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126360",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbadf8`](#insn-00bbadf8)

~~~json
{
  "source": "00bbadf8",
  "target": "00bbaeb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae00`](#insn-00bbae00)

~~~json
{
  "source": "00bbae00",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbae10`](#insn-00bbae10)

~~~json
{
  "source": "00bbae10",
  "target": "01126398",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126398",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbae14`](#insn-00bbae14)

~~~json
{
  "source": "00bbae14",
  "target": "011262b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011262b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbae18`](#insn-00bbae18)

~~~json
{
  "source": "00bbae18",
  "target": "00497a48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbae1c`](#insn-00bbae1c)

~~~json
{
  "source": "00bbae1c",
  "target": "01126398",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126398",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbae20`](#insn-00bbae20)

~~~json
{
  "source": "00bbae20",
  "target": "011262c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011262c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbae30`](#insn-00bbae30)

~~~json
{
  "source": "00bbae30",
  "target": "00574cec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbae34`](#insn-00bbae34)

~~~json
{
  "source": "00bbae34",
  "target": "00bbaea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae38`](#insn-00bbae38)

~~~json
{
  "source": "00bbae38",
  "target": "01126360",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126360",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbae3c`](#insn-00bbae3c)

~~~json
{
  "source": "00bbae3c",
  "target": "00bbae60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae44`](#insn-00bbae44)

~~~json
{
  "source": "00bbae44",
  "target": "002a2915",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2915",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "002a2915",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbae48`](#insn-00bbae48)

~~~json
{
  "source": "00bbae48",
  "target": "00c5aca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbae50`](#insn-00bbae50)

~~~json
{
  "source": "00bbae50",
  "target": "002b0777",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b0777",
  "offset": 0,
  "size": 27,
  "datatype": "string",
  "bytes": "4d6573736167696e67206e6f7420696e697469616c697a65642e00",
  "capture_start": "002b0777",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbae54`](#insn-00bbae54)

~~~json
{
  "source": "00bbae54",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbae58`](#insn-00bbae58)

~~~json
{
  "source": "00bbae58",
  "target": "01126360",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126360",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbae5c`](#insn-00bbae5c)

~~~json
{
  "source": "00bbae5c",
  "target": "00bbae7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae60`](#insn-00bbae60)

~~~json
{
  "source": "00bbae60",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbae68`](#insn-00bbae68)

~~~json
{
  "source": "00bbae68",
  "target": "01126398",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126398",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbae6c`](#insn-00bbae6c)

~~~json
{
  "source": "00bbae6c",
  "target": "011262b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011262b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbae70`](#insn-00bbae70)

~~~json
{
  "source": "00bbae70",
  "target": "00497a48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbae78`](#insn-00bbae78)

~~~json
{
  "source": "00bbae78",
  "target": "00bbaea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae7c`](#insn-00bbae7c)

~~~json
{
  "source": "00bbae7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae80`](#insn-00bbae80)

~~~json
{
  "source": "00bbae80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae84`](#insn-00bbae84)

~~~json
{
  "source": "00bbae84",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae8c`](#insn-00bbae8c)

~~~json
{
  "source": "00bbae8c",
  "target": "00bbaf50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaea0`](#insn-00bbaea0)

~~~json
{
  "source": "00bbaea0",
  "target": "01126400",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126400",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbaea4`](#insn-00bbaea4)

~~~json
{
  "source": "00bbaea4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaea8`](#insn-00bbaea8)

~~~json
{
  "source": "00bbaea8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaeac`](#insn-00bbaeac)

~~~json
{
  "source": "00bbaeac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaec0`](#insn-00bbaec0)

~~~json
{
  "source": "00bbaec0",
  "target": "01126398",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126398",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbaec4`](#insn-00bbaec4)

~~~json
{
  "source": "00bbaec4",
  "target": "011262c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011262c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbaed0`](#insn-00bbaed0)

~~~json
{
  "source": "00bbaed0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaed4`](#insn-00bbaed4)

~~~json
{
  "source": "00bbaed4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaed8`](#insn-00bbaed8)

~~~json
{
  "source": "00bbaed8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaee0`](#insn-00bbaee0)

~~~json
{
  "source": "00bbaee0",
  "target": "00574cec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
