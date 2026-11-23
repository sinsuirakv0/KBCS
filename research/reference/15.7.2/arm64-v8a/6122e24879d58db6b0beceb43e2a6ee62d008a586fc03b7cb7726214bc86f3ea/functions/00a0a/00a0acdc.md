# 00a0acdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a0acdc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0a/00a0acdc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/no_difference_in_scope-0018.md#compare-4d9821a3f08bd75f16c03a8bd185ee38)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a0acdc",
  "name": "FUN_00a0acdc",
  "size": 256,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0446610eac66ad2109b41d950116ea9ac1dc16629308f2e77e10dc3e3ff790f7",
  "source_text_sha256": "0446610eac66ad2109b41d950116ea9ac1dc16629308f2e77e10dc3e3ff790f7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a0acdc",
        "00a0addb"
      ]
    ],
    "bytes_sha256": "7d0dea4d841a6d10de1c22be91d5f9f81549af8c0bce991ef71f1b8363533dbf",
    "instruction_count": 64,
    "instruction_bytes": 256,
    "body_bytes": 256,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a0baf4](../00a0b/00a0baf4.md)

## 呼び出し先

- [0041fdf0](../0041f/0041fdf0.md)

## 関連文字列（未確認候補）

~~~text
"map::at:  key not found"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2297 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

undefined4 FUN_00a0acdc(long param_1,int param_2,int param_3)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  
                    /* try { // try from 00a0acdc to 00b0ace3 has its CatchHandler @ 00a0d5b0 */
  plVar1 = *(long **)(param_1 + 0x10);
  plVar2 = plVar1;
  do {
    if (plVar2 == (long *)0x0) {
      return 0;
    }
    if (*(int *)(plVar2 + 4) <= param_2) {
                    /* try { // try from 00a0ad08 to 00b0ad0f has its CatchHandler @ 00a0d5dc */
      plVar3 = plVar1;
      if (param_2 <= *(int *)(plVar2 + 4)) break;
      plVar2 = plVar2 + 1;
    }
    plVar2 = (long *)*plVar2;
  } while( true );
  while (plVar3 != (long *)0x0) {
    if (param_2 < (int)plVar3[4]) {
      plVar3 = (long *)*plVar3;
    }
    else {
      if (param_2 <= (int)plVar3[4]) {
        plVar2 = (long *)plVar3[6];
        goto joined_r0x00a0ad4c;
      }
      plVar3 = (long *)plVar3[1];
    }
  }
  goto LAB_00a0ad3c;
joined_r0x00a0ad4c:
  if (plVar2 == (long *)0x0) {
    return 0;
  }
                    /* try { // try from 00a0ad68 to 00b0aebb has its CatchHandler @ 00a0a31c */
  if (*(int *)((long)plVar2 + 0x1c) <= param_3) {
    if (param_3 <= *(int *)((long)plVar2 + 0x1c)) goto LAB_00a0ad84;
    plVar2 = plVar2 + 1;
  }
                    /* try { // try from 00a0ad60 to 00b0ad67 has its CatchHandler @ 00a0d5bc */
  plVar2 = (long *)*plVar2;
  goto joined_r0x00a0ad4c;
LAB_00a0ad84:
  do {
    if (param_2 < (int)plVar1[4]) {
      plVar1 = (long *)*plVar1;
    }
    else {
      if (param_2 <= (int)plVar1[4]) {
        for (plVar2 = (long *)plVar1[6]; plVar2 != (long *)0x0; plVar2 = (long *)*plVar2) {
          while (*(int *)((long)plVar2 + 0x1c) <= param_3) {
            if (param_3 <= *(int *)((long)plVar2 + 0x1c)) {
              return (int)plVar2[4];
            }
            plVar2 = (long *)plVar2[1];
            if (plVar2 == (long *)0x0) goto LAB_00a0ad3c;
          }
        }
        break;
      }
      plVar1 = (long *)plVar1[1];
    }
  } while (plVar1 != (long *)0x0);
LAB_00a0ad3c:
                    /* try { // try from 00a0ad3c to 00b0ad43 has its CatchHandler @ 00a0d5b4 */
                    /* WARNING: Subroutine does not return */
  FUN_0041fdf0("map::at:  key not found");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a0acdc"></a> `00a0acdc` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00a0ace0"></a> `00a0ace0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a0ace4"></a> `00a0ace4` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00a0ace8"></a> `00a0ace8` | `48 03 00 b4` | cbz x8,0x00a0ad50 | `CONDITIONAL_JUMP`
<a id="insn-00a0acec"></a> `00a0acec` | `e9 03 08 aa` | mov x9,x8 | `FALL_THROUGH`
<a id="insn-00a0acf0"></a> `00a0acf0` | `03 00 00 14` | b 0x00a0acfc | `UNCONDITIONAL_JUMP`
<a id="insn-00a0acf4"></a> `00a0acf4` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00a0acf8"></a> `00a0acf8` | `c9 02 00 b4` | cbz x9,0x00a0ad50 | `CONDITIONAL_JUMP`
<a id="insn-00a0acfc"></a> `00a0acfc` | `2a 21 40 b9` | ldr w10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00a0ad00"></a> `00a0ad00` | `5f 01 01 6b` | cmp w10,w1 | `FALL_THROUGH`
<a id="insn-00a0ad04"></a> `00a0ad04` | `8c ff ff 54` | b.gt 0x00a0acf4 | `CONDITIONAL_JUMP`
<a id="insn-00a0ad08"></a> `00a0ad08` | `6a 00 00 54` | b.ge 0x00a0ad14 | `CONDITIONAL_JUMP`
<a id="insn-00a0ad0c"></a> `00a0ad0c` | `29 21 00 91` | add x9,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00a0ad10"></a> `00a0ad10` | `f9 ff ff 17` | b 0x00a0acf4 | `UNCONDITIONAL_JUMP`
<a id="insn-00a0ad14"></a> `00a0ad14` | `e9 03 08 aa` | mov x9,x8 | `FALL_THROUGH`
<a id="insn-00a0ad18"></a> `00a0ad18` | `03 00 00 14` | b 0x00a0ad24 | `UNCONDITIONAL_JUMP`
<a id="insn-00a0ad1c"></a> `00a0ad1c` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00a0ad20"></a> `00a0ad20` | `e9 00 00 b4` | cbz x9,0x00a0ad3c | `CONDITIONAL_JUMP`
<a id="insn-00a0ad24"></a> `00a0ad24` | `2a 21 40 b9` | ldr w10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00a0ad28"></a> `00a0ad28` | `5f 01 01 6b` | cmp w10,w1 | `FALL_THROUGH`
<a id="insn-00a0ad2c"></a> `00a0ad2c` | `8c ff ff 54` | b.gt 0x00a0ad1c | `CONDITIONAL_JUMP`
<a id="insn-00a0ad30"></a> `00a0ad30` | `ca 00 00 54` | b.ge 0x00a0ad48 | `CONDITIONAL_JUMP`
<a id="insn-00a0ad34"></a> `00a0ad34` | `29 05 40 f9` | ldr x9,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00a0ad38"></a> `00a0ad38` | `69 ff ff b5` | cbnz x9,0x00a0ad24 | `CONDITIONAL_JUMP`
<a id="insn-00a0ad3c"></a> `00a0ad3c` | `20 c4 ff d0` | adrp x0,0x290000 | `FALL_THROUGH`
<a id="insn-00a0ad40"></a> `00a0ad40` | `00 b8 2e 91` | add x0,x0,#0xbae | `FALL_THROUGH`
<a id="insn-00a0ad44"></a> `00a0ad44` | `2b 54 e8 97` | bl 0x0041fdf0 | `CALL_TERMINATOR`
<a id="insn-00a0ad48"></a> `00a0ad48` | `29 19 40 f9` | ldr x9,[x9, #0x30] | `FALL_THROUGH`
<a id="insn-00a0ad4c"></a> `00a0ad4c` | `e9 00 00 b5` | cbnz x9,0x00a0ad68 | `CONDITIONAL_JUMP`
<a id="insn-00a0ad50"></a> `00a0ad50` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00a0ad54"></a> `00a0ad54` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00a0ad58"></a> `00a0ad58` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a0ad5c"></a> `00a0ad5c` | `29 21 00 91` | add x9,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00a0ad60"></a> `00a0ad60` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00a0ad64"></a> `00a0ad64` | `69 ff ff b4` | cbz x9,0x00a0ad50 | `CONDITIONAL_JUMP`
<a id="insn-00a0ad68"></a> `00a0ad68` | `2a 1d 40 b9` | ldr w10,[x9, #0x1c] | `FALL_THROUGH`
<a id="insn-00a0ad6c"></a> `00a0ad6c` | `5f 01 02 6b` | cmp w10,w2 | `FALL_THROUGH`
<a id="insn-00a0ad70"></a> `00a0ad70` | `8c ff ff 54` | b.gt 0x00a0ad60 | `CONDITIONAL_JUMP`
<a id="insn-00a0ad74"></a> `00a0ad74` | `4b ff ff 54` | b.lt 0x00a0ad5c | `CONDITIONAL_JUMP`
<a id="insn-00a0ad78"></a> `00a0ad78` | `03 00 00 14` | b 0x00a0ad84 | `UNCONDITIONAL_JUMP`
<a id="insn-00a0ad7c"></a> `00a0ad7c` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00a0ad80"></a> `00a0ad80` | `e8 fd ff b4` | cbz x8,0x00a0ad3c | `CONDITIONAL_JUMP`
<a id="insn-00a0ad84"></a> `00a0ad84` | `09 21 40 b9` | ldr w9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00a0ad88"></a> `00a0ad88` | `3f 01 01 6b` | cmp w9,w1 | `FALL_THROUGH`
<a id="insn-00a0ad8c"></a> `00a0ad8c` | `8c ff ff 54` | b.gt 0x00a0ad7c | `CONDITIONAL_JUMP`
<a id="insn-00a0ad90"></a> `00a0ad90` | `8a 00 00 54` | b.ge 0x00a0ada0 | `CONDITIONAL_JUMP`
<a id="insn-00a0ad94"></a> `00a0ad94` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00a0ad98"></a> `00a0ad98` | `68 ff ff b5` | cbnz x8,0x00a0ad84 | `CONDITIONAL_JUMP`
<a id="insn-00a0ad9c"></a> `00a0ad9c` | `e8 ff ff 17` | b 0x00a0ad3c | `UNCONDITIONAL_JUMP`
<a id="insn-00a0ada0"></a> `00a0ada0` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00a0ada4"></a> `00a0ada4` | `88 00 00 b5` | cbnz x8,0x00a0adb4 | `CONDITIONAL_JUMP`
<a id="insn-00a0ada8"></a> `00a0ada8` | `e5 ff ff 17` | b 0x00a0ad3c | `UNCONDITIONAL_JUMP`
<a id="insn-00a0adac"></a> `00a0adac` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00a0adb0"></a> `00a0adb0` | `68 fc ff b4` | cbz x8,0x00a0ad3c | `CONDITIONAL_JUMP`
<a id="insn-00a0adb4"></a> `00a0adb4` | `09 1d 40 b9` | ldr w9,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00a0adb8"></a> `00a0adb8` | `3f 01 02 6b` | cmp w9,w2 | `FALL_THROUGH`
<a id="insn-00a0adbc"></a> `00a0adbc` | `8c ff ff 54` | b.gt 0x00a0adac | `CONDITIONAL_JUMP`
<a id="insn-00a0adc0"></a> `00a0adc0` | `8a 00 00 54` | b.ge 0x00a0add0 | `CONDITIONAL_JUMP`
<a id="insn-00a0adc4"></a> `00a0adc4` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00a0adc8"></a> `00a0adc8` | `68 ff ff b5` | cbnz x8,0x00a0adb4 | `CONDITIONAL_JUMP`
<a id="insn-00a0adcc"></a> `00a0adcc` | `dc ff ff 17` | b 0x00a0ad3c | `UNCONDITIONAL_JUMP`
<a id="insn-00a0add0"></a> `00a0add0` | `00 21 40 b9` | ldr w0,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00a0add4"></a> `00a0add4` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00a0add8"></a> `00a0add8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a0acdc`](#insn-00a0acdc) 範囲 `[['00a0acdc', '00a0aceb']]`
  - `CONDITIONAL_JUMP` [`00a0ace8`](#insn-00a0ace8) → [`00a0ad50`](#insn-00a0ad50)
  - `FALL_THROUGH` [`00a0ace8`](#insn-00a0ace8) → [`00a0acec`](#insn-00a0acec)
- ブロック [`00a0acec`](#insn-00a0acec) 範囲 `[['00a0acec', '00a0acf3']]`
  - `UNCONDITIONAL_JUMP` [`00a0acf0`](#insn-00a0acf0) → [`00a0acfc`](#insn-00a0acfc)
- ブロック [`00a0acf4`](#insn-00a0acf4) 範囲 `[['00a0acf4', '00a0acfb']]`
  - `CONDITIONAL_JUMP` [`00a0acf8`](#insn-00a0acf8) → [`00a0ad50`](#insn-00a0ad50)
  - `FALL_THROUGH` [`00a0acf8`](#insn-00a0acf8) → [`00a0acfc`](#insn-00a0acfc)
- ブロック [`00a0acfc`](#insn-00a0acfc) 範囲 `[['00a0acfc', '00a0ad07']]`
  - `CONDITIONAL_JUMP` [`00a0ad04`](#insn-00a0ad04) → [`00a0acf4`](#insn-00a0acf4)
  - `FALL_THROUGH` [`00a0ad04`](#insn-00a0ad04) → [`00a0ad08`](#insn-00a0ad08)
- ブロック [`00a0ad08`](#insn-00a0ad08) 範囲 `[['00a0ad08', '00a0ad0b']]`
  - `CONDITIONAL_JUMP` [`00a0ad08`](#insn-00a0ad08) → [`00a0ad14`](#insn-00a0ad14)
  - `FALL_THROUGH` [`00a0ad08`](#insn-00a0ad08) → [`00a0ad0c`](#insn-00a0ad0c)
- ブロック [`00a0ad0c`](#insn-00a0ad0c) 範囲 `[['00a0ad0c', '00a0ad13']]`
  - `UNCONDITIONAL_JUMP` [`00a0ad10`](#insn-00a0ad10) → [`00a0acf4`](#insn-00a0acf4)
- ブロック [`00a0ad14`](#insn-00a0ad14) 範囲 `[['00a0ad14', '00a0ad1b']]`
  - `UNCONDITIONAL_JUMP` [`00a0ad18`](#insn-00a0ad18) → [`00a0ad24`](#insn-00a0ad24)
- ブロック [`00a0ad1c`](#insn-00a0ad1c) 範囲 `[['00a0ad1c', '00a0ad23']]`
  - `CONDITIONAL_JUMP` [`00a0ad20`](#insn-00a0ad20) → [`00a0ad3c`](#insn-00a0ad3c)
  - `FALL_THROUGH` [`00a0ad20`](#insn-00a0ad20) → [`00a0ad24`](#insn-00a0ad24)
- ブロック [`00a0ad24`](#insn-00a0ad24) 範囲 `[['00a0ad24', '00a0ad2f']]`
  - `CONDITIONAL_JUMP` [`00a0ad2c`](#insn-00a0ad2c) → [`00a0ad1c`](#insn-00a0ad1c)
  - `FALL_THROUGH` [`00a0ad2c`](#insn-00a0ad2c) → [`00a0ad30`](#insn-00a0ad30)
- ブロック [`00a0ad30`](#insn-00a0ad30) 範囲 `[['00a0ad30', '00a0ad33']]`
  - `CONDITIONAL_JUMP` [`00a0ad30`](#insn-00a0ad30) → [`00a0ad48`](#insn-00a0ad48)
  - `FALL_THROUGH` [`00a0ad30`](#insn-00a0ad30) → [`00a0ad34`](#insn-00a0ad34)
- ブロック [`00a0ad34`](#insn-00a0ad34) 範囲 `[['00a0ad34', '00a0ad3b']]`
  - `CONDITIONAL_JUMP` [`00a0ad38`](#insn-00a0ad38) → [`00a0ad24`](#insn-00a0ad24)
  - `FALL_THROUGH` [`00a0ad38`](#insn-00a0ad38) → [`00a0ad3c`](#insn-00a0ad3c)
- ブロック [`00a0ad3c`](#insn-00a0ad3c) 範囲 `[['00a0ad3c', '00a0ad47']]`
- ブロック [`00a0ad48`](#insn-00a0ad48) 範囲 `[['00a0ad48', '00a0ad4f']]`
  - `CONDITIONAL_JUMP` [`00a0ad4c`](#insn-00a0ad4c) → [`00a0ad68`](#insn-00a0ad68)
  - `FALL_THROUGH` [`00a0ad4c`](#insn-00a0ad4c) → [`00a0ad50`](#insn-00a0ad50)
- ブロック [`00a0ad50`](#insn-00a0ad50) 範囲 `[['00a0ad50', '00a0ad5b']]`
- ブロック [`00a0ad5c`](#insn-00a0ad5c) 範囲 `[['00a0ad5c', '00a0ad5f']]`
  - `FALL_THROUGH` [`00a0ad5c`](#insn-00a0ad5c) → [`00a0ad60`](#insn-00a0ad60)
- ブロック [`00a0ad60`](#insn-00a0ad60) 範囲 `[['00a0ad60', '00a0ad67']]`
  - `CONDITIONAL_JUMP` [`00a0ad64`](#insn-00a0ad64) → [`00a0ad50`](#insn-00a0ad50)
  - `FALL_THROUGH` [`00a0ad64`](#insn-00a0ad64) → [`00a0ad68`](#insn-00a0ad68)
- ブロック [`00a0ad68`](#insn-00a0ad68) 範囲 `[['00a0ad68', '00a0ad73']]`
  - `CONDITIONAL_JUMP` [`00a0ad70`](#insn-00a0ad70) → [`00a0ad60`](#insn-00a0ad60)
  - `FALL_THROUGH` [`00a0ad70`](#insn-00a0ad70) → [`00a0ad74`](#insn-00a0ad74)
- ブロック [`00a0ad74`](#insn-00a0ad74) 範囲 `[['00a0ad74', '00a0ad77']]`
  - `CONDITIONAL_JUMP` [`00a0ad74`](#insn-00a0ad74) → [`00a0ad5c`](#insn-00a0ad5c)
  - `FALL_THROUGH` [`00a0ad74`](#insn-00a0ad74) → [`00a0ad78`](#insn-00a0ad78)
- ブロック [`00a0ad78`](#insn-00a0ad78) 範囲 `[['00a0ad78', '00a0ad7b']]`
  - `UNCONDITIONAL_JUMP` [`00a0ad78`](#insn-00a0ad78) → [`00a0ad84`](#insn-00a0ad84)
- ブロック [`00a0ad7c`](#insn-00a0ad7c) 範囲 `[['00a0ad7c', '00a0ad83']]`
  - `CONDITIONAL_JUMP` [`00a0ad80`](#insn-00a0ad80) → [`00a0ad3c`](#insn-00a0ad3c)
  - `FALL_THROUGH` [`00a0ad80`](#insn-00a0ad80) → [`00a0ad84`](#insn-00a0ad84)
- ブロック [`00a0ad84`](#insn-00a0ad84) 範囲 `[['00a0ad84', '00a0ad8f']]`
  - `CONDITIONAL_JUMP` [`00a0ad8c`](#insn-00a0ad8c) → [`00a0ad7c`](#insn-00a0ad7c)
  - `FALL_THROUGH` [`00a0ad8c`](#insn-00a0ad8c) → [`00a0ad90`](#insn-00a0ad90)
- ブロック [`00a0ad90`](#insn-00a0ad90) 範囲 `[['00a0ad90', '00a0ad93']]`
  - `CONDITIONAL_JUMP` [`00a0ad90`](#insn-00a0ad90) → [`00a0ada0`](#insn-00a0ada0)
  - `FALL_THROUGH` [`00a0ad90`](#insn-00a0ad90) → [`00a0ad94`](#insn-00a0ad94)
- ブロック [`00a0ad94`](#insn-00a0ad94) 範囲 `[['00a0ad94', '00a0ad9b']]`
  - `CONDITIONAL_JUMP` [`00a0ad98`](#insn-00a0ad98) → [`00a0ad84`](#insn-00a0ad84)
  - `FALL_THROUGH` [`00a0ad98`](#insn-00a0ad98) → [`00a0ad9c`](#insn-00a0ad9c)
- ブロック [`00a0ad9c`](#insn-00a0ad9c) 範囲 `[['00a0ad9c', '00a0ad9f']]`
  - `UNCONDITIONAL_JUMP` [`00a0ad9c`](#insn-00a0ad9c) → [`00a0ad3c`](#insn-00a0ad3c)
- ブロック [`00a0ada0`](#insn-00a0ada0) 範囲 `[['00a0ada0', '00a0ada7']]`
  - `CONDITIONAL_JUMP` [`00a0ada4`](#insn-00a0ada4) → [`00a0adb4`](#insn-00a0adb4)
  - `FALL_THROUGH` [`00a0ada4`](#insn-00a0ada4) → [`00a0ada8`](#insn-00a0ada8)
- ブロック [`00a0ada8`](#insn-00a0ada8) 範囲 `[['00a0ada8', '00a0adab']]`
  - `UNCONDITIONAL_JUMP` [`00a0ada8`](#insn-00a0ada8) → [`00a0ad3c`](#insn-00a0ad3c)
- ブロック [`00a0adac`](#insn-00a0adac) 範囲 `[['00a0adac', '00a0adb3']]`
  - `CONDITIONAL_JUMP` [`00a0adb0`](#insn-00a0adb0) → [`00a0ad3c`](#insn-00a0ad3c)
  - `FALL_THROUGH` [`00a0adb0`](#insn-00a0adb0) → [`00a0adb4`](#insn-00a0adb4)
- ブロック [`00a0adb4`](#insn-00a0adb4) 範囲 `[['00a0adb4', '00a0adbf']]`
  - `CONDITIONAL_JUMP` [`00a0adbc`](#insn-00a0adbc) → [`00a0adac`](#insn-00a0adac)
  - `FALL_THROUGH` [`00a0adbc`](#insn-00a0adbc) → [`00a0adc0`](#insn-00a0adc0)
- ブロック [`00a0adc0`](#insn-00a0adc0) 範囲 `[['00a0adc0', '00a0adc3']]`
  - `CONDITIONAL_JUMP` [`00a0adc0`](#insn-00a0adc0) → [`00a0add0`](#insn-00a0add0)
  - `FALL_THROUGH` [`00a0adc0`](#insn-00a0adc0) → [`00a0adc4`](#insn-00a0adc4)
- ブロック [`00a0adc4`](#insn-00a0adc4) 範囲 `[['00a0adc4', '00a0adcb']]`
  - `CONDITIONAL_JUMP` [`00a0adc8`](#insn-00a0adc8) → [`00a0adb4`](#insn-00a0adb4)
  - `FALL_THROUGH` [`00a0adc8`](#insn-00a0adc8) → [`00a0adcc`](#insn-00a0adcc)
- ブロック [`00a0adcc`](#insn-00a0adcc) 範囲 `[['00a0adcc', '00a0adcf']]`
  - `UNCONDITIONAL_JUMP` [`00a0adcc`](#insn-00a0adcc) → [`00a0ad3c`](#insn-00a0ad3c)
- ブロック [`00a0add0`](#insn-00a0add0) 範囲 `[['00a0add0', '00a0addb']]`

## 命令位置別の参照

- [`00a0acdc`](#insn-00a0acdc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ace8`](#insn-00a0ace8) → [`00a0ad50`](#insn-00a0ad50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0acf0`](#insn-00a0acf0) → [`00a0acfc`](#insn-00a0acfc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0acf8`](#insn-00a0acf8) → [`00a0ad50`](#insn-00a0ad50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad04`](#insn-00a0ad04) → [`00a0acf4`](#insn-00a0acf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad08`](#insn-00a0ad08) → [`00a0ad14`](#insn-00a0ad14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad10`](#insn-00a0ad10) → [`00a0acf4`](#insn-00a0acf4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad18`](#insn-00a0ad18) → [`00a0ad24`](#insn-00a0ad24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad20`](#insn-00a0ad20) → [`00a0ad3c`](#insn-00a0ad3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad2c`](#insn-00a0ad2c) → [`00a0ad1c`](#insn-00a0ad1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad30`](#insn-00a0ad30) → [`00a0ad48`](#insn-00a0ad48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad38`](#insn-00a0ad38) → [`00a0ad24`](#insn-00a0ad24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad40`](#insn-00a0ad40) → `00290bae`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a0ad44`](#insn-00a0ad44) → [`0041fdf0`](../0041f/0041fdf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041fdf0` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad4c`](#insn-00a0ad4c) → [`00a0ad68`](#insn-00a0ad68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad54`](#insn-00a0ad54) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad64`](#insn-00a0ad64) → [`00a0ad50`](#insn-00a0ad50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad70`](#insn-00a0ad70) → [`00a0ad60`](#insn-00a0ad60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad74`](#insn-00a0ad74) → [`00a0ad5c`](#insn-00a0ad5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad78`](#insn-00a0ad78) → [`00a0ad84`](#insn-00a0ad84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad80`](#insn-00a0ad80) → [`00a0ad3c`](#insn-00a0ad3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad8c`](#insn-00a0ad8c) → [`00a0ad7c`](#insn-00a0ad7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad90`](#insn-00a0ad90) → [`00a0ada0`](#insn-00a0ada0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad98`](#insn-00a0ad98) → [`00a0ad84`](#insn-00a0ad84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad9c`](#insn-00a0ad9c) → [`00a0ad3c`](#insn-00a0ad3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ada4`](#insn-00a0ada4) → [`00a0adb4`](#insn-00a0adb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ada8`](#insn-00a0ada8) → [`00a0ad3c`](#insn-00a0ad3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0adb0`](#insn-00a0adb0) → [`00a0ad3c`](#insn-00a0ad3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0adbc`](#insn-00a0adbc) → [`00a0adac`](#insn-00a0adac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0adc0`](#insn-00a0adc0) → [`00a0add0`](#insn-00a0add0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0adc8`](#insn-00a0adc8) → [`00a0adb4`](#insn-00a0adb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0adcc`](#insn-00a0adcc) → [`00a0ad3c`](#insn-00a0ad3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0add4`](#insn-00a0add4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a0acdc`](#insn-00a0acdc)

~~~json
{
  "source": "00a0acdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ace8`](#insn-00a0ace8)

~~~json
{
  "source": "00a0ace8",
  "target": "00a0ad50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0acf0`](#insn-00a0acf0)

~~~json
{
  "source": "00a0acf0",
  "target": "00a0acfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0acf8`](#insn-00a0acf8)

~~~json
{
  "source": "00a0acf8",
  "target": "00a0ad50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad04`](#insn-00a0ad04)

~~~json
{
  "source": "00a0ad04",
  "target": "00a0acf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad08`](#insn-00a0ad08)

~~~json
{
  "source": "00a0ad08",
  "target": "00a0ad14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad10`](#insn-00a0ad10)

~~~json
{
  "source": "00a0ad10",
  "target": "00a0acf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad18`](#insn-00a0ad18)

~~~json
{
  "source": "00a0ad18",
  "target": "00a0ad24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad20`](#insn-00a0ad20)

~~~json
{
  "source": "00a0ad20",
  "target": "00a0ad3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad2c`](#insn-00a0ad2c)

~~~json
{
  "source": "00a0ad2c",
  "target": "00a0ad1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad30`](#insn-00a0ad30)

~~~json
{
  "source": "00a0ad30",
  "target": "00a0ad48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad38`](#insn-00a0ad38)

~~~json
{
  "source": "00a0ad38",
  "target": "00a0ad24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad40`](#insn-00a0ad40)

~~~json
{
  "source": "00a0ad40",
  "target": "00290bae",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00290bae",
  "offset": 0,
  "size": 24,
  "datatype": "string",
  "bytes": "6d61703a3a61743a20206b6579206e6f7420666f756e6400",
  "capture_start": "00290bae",
  "capture_bytes": 24,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a0ad44`](#insn-00a0ad44)

~~~json
{
  "source": "00a0ad44",
  "target": "0041fdf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ad4c`](#insn-00a0ad4c)

~~~json
{
  "source": "00a0ad4c",
  "target": "00a0ad68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad54`](#insn-00a0ad54)

~~~json
{
  "source": "00a0ad54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad64`](#insn-00a0ad64)

~~~json
{
  "source": "00a0ad64",
  "target": "00a0ad50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad70`](#insn-00a0ad70)

~~~json
{
  "source": "00a0ad70",
  "target": "00a0ad60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad74`](#insn-00a0ad74)

~~~json
{
  "source": "00a0ad74",
  "target": "00a0ad5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad78`](#insn-00a0ad78)

~~~json
{
  "source": "00a0ad78",
  "target": "00a0ad84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad80`](#insn-00a0ad80)

~~~json
{
  "source": "00a0ad80",
  "target": "00a0ad3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad8c`](#insn-00a0ad8c)

~~~json
{
  "source": "00a0ad8c",
  "target": "00a0ad7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad90`](#insn-00a0ad90)

~~~json
{
  "source": "00a0ad90",
  "target": "00a0ada0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad98`](#insn-00a0ad98)

~~~json
{
  "source": "00a0ad98",
  "target": "00a0ad84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad9c`](#insn-00a0ad9c)

~~~json
{
  "source": "00a0ad9c",
  "target": "00a0ad3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ada4`](#insn-00a0ada4)

~~~json
{
  "source": "00a0ada4",
  "target": "00a0adb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ada8`](#insn-00a0ada8)

~~~json
{
  "source": "00a0ada8",
  "target": "00a0ad3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0adb0`](#insn-00a0adb0)

~~~json
{
  "source": "00a0adb0",
  "target": "00a0ad3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0adbc`](#insn-00a0adbc)

~~~json
{
  "source": "00a0adbc",
  "target": "00a0adac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0adc0`](#insn-00a0adc0)

~~~json
{
  "source": "00a0adc0",
  "target": "00a0add0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0adc8`](#insn-00a0adc8)

~~~json
{
  "source": "00a0adc8",
  "target": "00a0adb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0adcc`](#insn-00a0adcc)

~~~json
{
  "source": "00a0adcc",
  "target": "00a0ad3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0add4`](#insn-00a0add4)

~~~json
{
  "source": "00a0add4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
