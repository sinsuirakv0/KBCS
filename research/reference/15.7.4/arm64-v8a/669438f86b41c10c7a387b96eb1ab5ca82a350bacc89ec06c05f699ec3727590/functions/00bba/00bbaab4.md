# 00bbaab4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbaa70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa70.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-fe515bab60102bd67df3aacb51e14157)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c374fc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374fc.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0077.md#compare-5e740a8f7cb7b9f7e59c8b72f300a976)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaab4",
  "name": "FUN_00bbaab4",
  "size": 292,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d5ac710da9b9a8d8f95bd4b7134ae17adb839666a464949512e725ac44a2670b",
  "source_text_sha256": "d5ac710da9b9a8d8f95bd4b7134ae17adb839666a464949512e725ac44a2670b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbaab4",
        "00bbabd7"
      ]
    ],
    "bytes_sha256": "838e069d5c263cd656647bd53a805377675d8bd8936467bf47ad18901f3f4200",
    "instruction_count": 73,
    "instruction_bytes": 292,
    "body_bytes": 292,
    "indirect": 2,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bbb19c](../00bbb/00bbb19c.md)
- [00bbb4c0](../00bbb/00bbb4c0.md)
- [00bd4fd8](../00bd4/00bd4fd8.md)
- [00bd4fe4](../00bd4/00bd4fe4.md)
- [00be1de0](../00be1/00be1de0.md)
- [00be1e30](../00be1/00be1e30.md)

## 関連文字列（未確認候補）

~~~text
"terminating"
"terminating due to %s exception of type %s"
"terminating due to %s exception of type %s: %s"
"terminating due to %s foreign exception"
"uncaught"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4423 bytes

~~~c

void FUN_00bbaab4(void)

{
  undefined *puVar1;
  long *plVar2;
  ulong uVar3;
  long lVar4;
  undefined8 uVar5;
  long lVar6;
  long lVar7;
  long *local_18;
  
                    /* catch() { ... } // from try @ 00bb56cc with catch @ 00bbaab8 */
                    /* catch() { ... } // from try @ 00bb9e30 with catch @ 00bbaabc */
  plVar2 = (long *)__cxa_get_globals_fast();
                    /* catch() { ... } // from try @ 00bb9e24 with catch @ 00bbaad0 */
  if ((plVar2 == (long *)0x0) || (lVar6 = *plVar2, lVar6 == 0)) {
                    /* catch() { ... } // from try @ 00bb9ec0 with catch @ 00bbaad8 */
                    /* WARNING: Subroutine does not return */
    FUN_00bbb19c("terminating");
  }
  uVar3 = FUN_00bd4fe4(lVar6 + 0x60);
                    /* catch() { ... } // from try @ 00bb9eb0 with catch @ 00bbaaec */
  if ((uVar3 & 1) == 0) {
                    /* catch() { ... } // from try @ 00bb9a78 with catch @ 00bbab24 */
                    /* WARNING: Subroutine does not return */
    FUN_00bbb19c("terminating due to %s foreign exception",PTR_s_uncaught_00c249a0);
  }
                    /* catch() { ... } // from try @ 00bb9a00 with catch @ 00bbaaf4 */
  lVar4 = FUN_00bd4fd8(lVar6 + 0x60);
                    /* catch() { ... } // from try @ 00bb99f4 with catch @ 00bbab08 */
  if (lVar4 == 0x434c4e47432b2b01) {
                    /* catch() { ... } // from try @ 00bb9a88 with catch @ 00bbab10 */
    local_18 = *(long **)(lVar6 + 8);
  }
  else {
                    /* catch() { ... } // from try @ 00bba4d4 with catch @ 00bbab2c */
    local_18 = (long *)(lVar6 + 0x80);
  }
                    /* catch() { ... } // from try @ 00bb5630 with catch @ 00bbab30 */
  lVar7 = *(long *)(lVar6 + 0x10);
                    /* catch() { ... } // from try @ 00bb7c1c with catch @ 00bbab34 */
                    /* catch() { ... } // from try @ 00bb5544 with catch @ 00bbab38 */
                    /* catch() { ... } // from try @ 00bb552c with catch @ 00bbab3c */
                    /* catch() { ... } // from try @ 00bb551c with catch @ 00bbab40 */
                    /* catch() { ... } // from try @ 00bb3514 with catch @ 00bbab44 */
  lVar6 = *(long *)(lVar7 + 8);
                    /* catch() { ... } // from try @ 00bba014 with catch @ 00bbab48 */
                    /* catch() { ... } // from try @ 00bb9c90 with catch @ 00bbab4c */
  lVar4 = __cxa_demangle(lVar6,0,0,0);
                    /* catch() { ... } // from try @ 00bb9c84 with catch @ 00bbab60 */
                    /* catch() { ... } // from try @ 00bb9bd8 with catch @ 00bbab68 */
                    /* catch() { ... } // from try @ 00bb9bcc with catch @ 00bbab6c */
  if (lVar4 != 0) {
    lVar6 = lVar4;
  }
                    /* catch() { ... } // from try @ 00bb98bc with catch @ 00bbab70 */
                    /* catch() { ... } // from try @ 00bb98c8 with catch @ 00bbab78 */
  uVar3 = (**(code **)(*(long *)PTR__ZTISt9exception_00c1ae88 + 0x20))
                    (PTR__ZTISt9exception_00c1ae88,lVar7,&local_18);
  puVar1 = PTR_s_uncaught_00c249a0;
  if ((uVar3 & 1) != 0) {
    uVar5 = (**(code **)(*local_18 + 0x10))();
                    /* catch() { ... } // from try @ 00bb7674 with catch @ 00bbabac */
                    /* catch() { ... } // from try @ 00bb72c4 with catch @ 00bbabb0 */
                    /* catch() { ... } // from try @ 00bb6f10 with catch @ 00bbabb4 */
                    /* catch() { ... } // from try @ 00bb6b5c with catch @ 00bbabb8 */
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00bb67a8 with catch @ 00bbabbc */
    FUN_00bbb19c("terminating due to %s exception of type %s: %s",puVar1,lVar6,uVar5);
  }
                    /* catch() { ... } // from try @ 00bb63f4 with catch @ 00bbabc0 */
                    /* catch() { ... } // from try @ 00bb6040 with catch @ 00bbabc4 */
                    /* catch() { ... } // from try @ 00bb5c80 with catch @ 00bbabc8 */
                    /* catch() { ... } // from try @ 00bb58c0 with catch @ 00bbabcc */
                    /* catch() { ... } // from try @ 00bb5148 with catch @ 00bbabd0 */
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00bb4d68 with catch @ 00bbabd4 */
  FUN_00bbb19c("terminating due to %s exception of type %s",PTR_s_uncaught_00c249a0,lVar6);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbaab4"></a> `00bbaab4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbaab8"></a> `00bbaab8` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bbaabc"></a> `00bbaabc` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaac0"></a> `00bbaac0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbaac4"></a> `00bbaac4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbaac8"></a> `00bbaac8` | `c6 9c 00 94` | bl 0x00be1de0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaacc"></a> `00bbaacc` | `60 00 00 b4` | cbz x0,0x00bbaad8 | `CONDITIONAL_JUMP`
<a id="insn-00bbaad0"></a> `00bbaad0` | `13 00 40 f9` | ldr x19,[x0] | `FALL_THROUGH`
<a id="insn-00bbaad4"></a> `00bbaad4` | `93 00 00 b5` | cbnz x19,0x00bbaae4 | `CONDITIONAL_JUMP`
<a id="insn-00bbaad8"></a> `00bbaad8` | `a0 b7 ff d0` | adrp x0,0x2b0000 | `FALL_THROUGH`
<a id="insn-00bbaadc"></a> `00bbaadc` | `00 04 26 91` | add x0,x0,#0x981 | `FALL_THROUGH`
<a id="insn-00bbaae0"></a> `00bbaae0` | `af 01 00 94` | bl 0x00bbb19c | `CALL_TERMINATOR`
<a id="insn-00bbaae4"></a> `00bbaae4` | `60 82 01 91` | add x0,x19,#0x60 | `FALL_THROUGH`
<a id="insn-00bbaae8"></a> `00bbaae8` | `3f 69 00 94` | bl 0x00bd4fe4 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaaec"></a> `00bbaaec` | `60 01 00 36` | tbz w0,#0x0,0x00bbab18 | `CONDITIONAL_JUMP`
<a id="insn-00bbaaf0"></a> `00bbaaf0` | `60 82 01 91` | add x0,x19,#0x60 | `FALL_THROUGH`
<a id="insn-00bbaaf4"></a> `00bbaaf4` | `39 69 00 94` | bl 0x00bd4fd8 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaaf8"></a> `00bbaaf8` | `28 60 85 d2` | mov x8,#0x2b01 | `FALL_THROUGH`
<a id="insn-00bbaafc"></a> `00bbaafc` | `68 65 a8 f2` | movk x8,#0x432b, LSL #16 | `FALL_THROUGH`
<a id="insn-00bbab00"></a> `00bbab00` | `e8 c8 c9 f2` | movk x8,#0x4e47, LSL #32 | `FALL_THROUGH`
<a id="insn-00bbab04"></a> `00bbab04` | `88 69 e8 f2` | movk x8,#0x434c, LSL #48 | `FALL_THROUGH`
<a id="insn-00bbab08"></a> `00bbab08` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bbab0c"></a> `00bbab0c` | `01 01 00 54` | b.ne 0x00bbab2c | `CONDITIONAL_JUMP`
<a id="insn-00bbab10"></a> `00bbab10` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbab14"></a> `00bbab14` | `07 00 00 14` | b 0x00bbab30 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbab18"></a> `00bbab18` | `48 03 00 d0` | adrp x8,0xc24000 | `FALL_THROUGH`
<a id="insn-00bbab1c"></a> `00bbab1c` | `20 b7 ff d0` | adrp x0,0x2a0000 | `FALL_THROUGH`
<a id="insn-00bbab20"></a> `00bbab20` | `00 58 0b 91` | add x0,x0,#0x2d6 | `FALL_THROUGH`
<a id="insn-00bbab24"></a> `00bbab24` | `01 d1 44 f9` | ldr x1,[x8, #0x9a0] | `FALL_THROUGH`
<a id="insn-00bbab28"></a> `00bbab28` | `9d 01 00 94` | bl 0x00bbb19c | `CALL_TERMINATOR`
<a id="insn-00bbab2c"></a> `00bbab2c` | `68 02 02 91` | add x8,x19,#0x80 | `FALL_THROUGH`
<a id="insn-00bbab30"></a> `00bbab30` | `74 0a 40 f9` | ldr x20,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbab34"></a> `00bbab34` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbab38"></a> `00bbab38` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bbab3c"></a> `00bbab3c` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbab40"></a> `00bbab40` | `a8 0f 00 f9` | str x8,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bbab44"></a> `00bbab44` | `93 06 40 f9` | ldr x19,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbab48"></a> `00bbab48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbab4c"></a> `00bbab4c` | `b9 9c 00 94` | bl 0x00be1e30 | `UNCONDITIONAL_CALL`
<a id="insn-00bbab50"></a> `00bbab50` | `08 03 00 90` | adrp x8,0xc1a000 | `FALL_THROUGH`
<a id="insn-00bbab54"></a> `00bbab54` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-00bbab58"></a> `00bbab58` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bbab5c"></a> `00bbab5c` | `8a 0a 00 10` | adr x10,0xbbacac | `FALL_THROUGH`
<a id="insn-00bbab60"></a> `00bbab60` | `08 45 47 f9` | ldr x8,[x8, #0xe88] | `FALL_THROUGH`
<a id="insn-00bbab64"></a> `00bbab64` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bbab68"></a> `00bbab68` | `6b 0a 00 10` | adr x11,0xbbacb4 | `FALL_THROUGH`
<a id="insn-00bbab6c"></a> `00bbab6c` | `73 02 80 9a` | csel x19,x19,x0,eq | `FALL_THROUGH`
<a id="insn-00bbab70"></a> `00bbab70` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00bbab74"></a> `00bbab74` | `75 01 8a 9a` | csel x21,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00bbab78"></a> `00bbab78` | `29 11 40 f9` | ldr x9,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bbab7c"></a> `00bbab7c` | `a2 63 00 91` | add x2,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bbab80"></a> `00bbab80` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbab84"></a> `00bbab84` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbab88"></a> `00bbab88` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00bbab8c"></a> `00bbab8c` | `a0 01 00 36` | tbz w0,#0x0,0x00bbabc0 | `CONDITIONAL_JUMP`
<a id="insn-00bbab90"></a> `00bbab90` | `a0 0f 40 f9` | ldr x0,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bbab94"></a> `00bbab94` | `49 03 00 d0` | adrp x9,0xc24000 | `FALL_THROUGH`
<a id="insn-00bbab98"></a> `00bbab98` | `34 d1 44 f9` | ldr x20,[x9, #0x9a0] | `FALL_THROUGH`
<a id="insn-00bbab9c"></a> `00bbab9c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbaba0"></a> `00bbaba0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaba4"></a> `00bbaba4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbaba8"></a> `00bbaba8` | `e3 03 00 aa` | mov x3,x0 | `FALL_THROUGH`
<a id="insn-00bbabac"></a> `00bbabac` | `60 b7 ff f0` | adrp x0,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bbabb0"></a> `00bbabb0` | `00 20 05 91` | add x0,x0,#0x148 | `FALL_THROUGH`
<a id="insn-00bbabb4"></a> `00bbabb4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbabb8"></a> `00bbabb8` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bbabbc"></a> `00bbabbc` | `78 01 00 94` | bl 0x00bbb19c | `CALL_TERMINATOR`
<a id="insn-00bbabc0"></a> `00bbabc0` | `48 03 00 d0` | adrp x8,0xc24000 | `FALL_THROUGH`
<a id="insn-00bbabc4"></a> `00bbabc4` | `01 d1 44 f9` | ldr x1,[x8, #0x9a0] | `FALL_THROUGH`
<a id="insn-00bbabc8"></a> `00bbabc8` | `00 b7 ff d0` | adrp x0,0x29c000 | `FALL_THROUGH`
<a id="insn-00bbabcc"></a> `00bbabcc` | `00 74 0b 91` | add x0,x0,#0x2dd | `FALL_THROUGH`
<a id="insn-00bbabd0"></a> `00bbabd0` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bbabd4"></a> `00bbabd4` | `72 01 00 94` | bl 0x00bbb19c | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbaab4`](#insn-00bbaab4) 範囲 `[['00bbaab4', '00bbaab7']]`
  - `FALL_THROUGH` [`00bbaab4`](#insn-00bbaab4) → [`00bbaab8`](#insn-00bbaab8)
- ブロック [`00bbaab8`](#insn-00bbaab8) 範囲 `[['00bbaab8', '00bbaabb']]`
  - `FALL_THROUGH` [`00bbaab8`](#insn-00bbaab8) → [`00bbaabc`](#insn-00bbaabc)
- ブロック [`00bbaabc`](#insn-00bbaabc) 範囲 `[['00bbaabc', '00bbaacf']]`
  - `CONDITIONAL_JUMP` [`00bbaacc`](#insn-00bbaacc) → [`00bbaad8`](#insn-00bbaad8)
  - `FALL_THROUGH` [`00bbaacc`](#insn-00bbaacc) → [`00bbaad0`](#insn-00bbaad0)
- ブロック [`00bbaad0`](#insn-00bbaad0) 範囲 `[['00bbaad0', '00bbaad7']]`
  - `CONDITIONAL_JUMP` [`00bbaad4`](#insn-00bbaad4) → [`00bbaae4`](#insn-00bbaae4)
  - `FALL_THROUGH` [`00bbaad4`](#insn-00bbaad4) → [`00bbaad8`](#insn-00bbaad8)
- ブロック [`00bbaad8`](#insn-00bbaad8) 範囲 `[['00bbaad8', '00bbaae3']]`
- ブロック [`00bbaae4`](#insn-00bbaae4) 範囲 `[['00bbaae4', '00bbaaeb']]`
  - `FALL_THROUGH` [`00bbaae8`](#insn-00bbaae8) → [`00bbaaec`](#insn-00bbaaec)
- ブロック [`00bbaaec`](#insn-00bbaaec) 範囲 `[['00bbaaec', '00bbaaef']]`
  - `CONDITIONAL_JUMP` [`00bbaaec`](#insn-00bbaaec) → [`00bbab18`](#insn-00bbab18)
  - `FALL_THROUGH` [`00bbaaec`](#insn-00bbaaec) → [`00bbaaf0`](#insn-00bbaaf0)
- ブロック [`00bbaaf0`](#insn-00bbaaf0) 範囲 `[['00bbaaf0', '00bbaaf3']]`
  - `FALL_THROUGH` [`00bbaaf0`](#insn-00bbaaf0) → [`00bbaaf4`](#insn-00bbaaf4)
- ブロック [`00bbaaf4`](#insn-00bbaaf4) 範囲 `[['00bbaaf4', '00bbab07']]`
  - `FALL_THROUGH` [`00bbab04`](#insn-00bbab04) → [`00bbab08`](#insn-00bbab08)
- ブロック [`00bbab08`](#insn-00bbab08) 範囲 `[['00bbab08', '00bbab0f']]`
  - `CONDITIONAL_JUMP` [`00bbab0c`](#insn-00bbab0c) → [`00bbab2c`](#insn-00bbab2c)
  - `FALL_THROUGH` [`00bbab0c`](#insn-00bbab0c) → [`00bbab10`](#insn-00bbab10)
- ブロック [`00bbab10`](#insn-00bbab10) 範囲 `[['00bbab10', '00bbab17']]`
  - `UNCONDITIONAL_JUMP` [`00bbab14`](#insn-00bbab14) → [`00bbab30`](#insn-00bbab30)
- ブロック [`00bbab18`](#insn-00bbab18) 範囲 `[['00bbab18', '00bbab23']]`
  - `FALL_THROUGH` [`00bbab20`](#insn-00bbab20) → [`00bbab24`](#insn-00bbab24)
- ブロック [`00bbab24`](#insn-00bbab24) 範囲 `[['00bbab24', '00bbab2b']]`
- ブロック [`00bbab2c`](#insn-00bbab2c) 範囲 `[['00bbab2c', '00bbab2f']]`
  - `FALL_THROUGH` [`00bbab2c`](#insn-00bbab2c) → [`00bbab30`](#insn-00bbab30)
- ブロック [`00bbab30`](#insn-00bbab30) 範囲 `[['00bbab30', '00bbab33']]`
  - `FALL_THROUGH` [`00bbab30`](#insn-00bbab30) → [`00bbab34`](#insn-00bbab34)
- ブロック [`00bbab34`](#insn-00bbab34) 範囲 `[['00bbab34', '00bbab37']]`
  - `FALL_THROUGH` [`00bbab34`](#insn-00bbab34) → [`00bbab38`](#insn-00bbab38)
- ブロック [`00bbab38`](#insn-00bbab38) 範囲 `[['00bbab38', '00bbab3b']]`
  - `FALL_THROUGH` [`00bbab38`](#insn-00bbab38) → [`00bbab3c`](#insn-00bbab3c)
- ブロック [`00bbab3c`](#insn-00bbab3c) 範囲 `[['00bbab3c', '00bbab3f']]`
  - `FALL_THROUGH` [`00bbab3c`](#insn-00bbab3c) → [`00bbab40`](#insn-00bbab40)
- ブロック [`00bbab40`](#insn-00bbab40) 範囲 `[['00bbab40', '00bbab43']]`
  - `FALL_THROUGH` [`00bbab40`](#insn-00bbab40) → [`00bbab44`](#insn-00bbab44)
- ブロック [`00bbab44`](#insn-00bbab44) 範囲 `[['00bbab44', '00bbab47']]`
  - `FALL_THROUGH` [`00bbab44`](#insn-00bbab44) → [`00bbab48`](#insn-00bbab48)
- ブロック [`00bbab48`](#insn-00bbab48) 範囲 `[['00bbab48', '00bbab4b']]`
  - `FALL_THROUGH` [`00bbab48`](#insn-00bbab48) → [`00bbab4c`](#insn-00bbab4c)
- ブロック [`00bbab4c`](#insn-00bbab4c) 範囲 `[['00bbab4c', '00bbab5f']]`
  - `FALL_THROUGH` [`00bbab5c`](#insn-00bbab5c) → [`00bbab60`](#insn-00bbab60)
- ブロック [`00bbab60`](#insn-00bbab60) 範囲 `[['00bbab60', '00bbab67']]`
  - `FALL_THROUGH` [`00bbab64`](#insn-00bbab64) → [`00bbab68`](#insn-00bbab68)
- ブロック [`00bbab68`](#insn-00bbab68) 範囲 `[['00bbab68', '00bbab6b']]`
  - `FALL_THROUGH` [`00bbab68`](#insn-00bbab68) → [`00bbab6c`](#insn-00bbab6c)
- ブロック [`00bbab6c`](#insn-00bbab6c) 範囲 `[['00bbab6c', '00bbab6f']]`
  - `FALL_THROUGH` [`00bbab6c`](#insn-00bbab6c) → [`00bbab70`](#insn-00bbab70)
- ブロック [`00bbab70`](#insn-00bbab70) 範囲 `[['00bbab70', '00bbab77']]`
  - `FALL_THROUGH` [`00bbab74`](#insn-00bbab74) → [`00bbab78`](#insn-00bbab78)
- ブロック [`00bbab78`](#insn-00bbab78) 範囲 `[['00bbab78', '00bbab8f']]`
  - `CONDITIONAL_JUMP` [`00bbab8c`](#insn-00bbab8c) → [`00bbabc0`](#insn-00bbabc0)
  - `FALL_THROUGH` [`00bbab8c`](#insn-00bbab8c) → [`00bbab90`](#insn-00bbab90)
- ブロック [`00bbab90`](#insn-00bbab90) 範囲 `[['00bbab90', '00bbabab']]`
  - `FALL_THROUGH` [`00bbaba8`](#insn-00bbaba8) → [`00bbabac`](#insn-00bbabac)
- ブロック [`00bbabac`](#insn-00bbabac) 範囲 `[['00bbabac', '00bbabaf']]`
  - `FALL_THROUGH` [`00bbabac`](#insn-00bbabac) → [`00bbabb0`](#insn-00bbabb0)
- ブロック [`00bbabb0`](#insn-00bbabb0) 範囲 `[['00bbabb0', '00bbabb3']]`
  - `FALL_THROUGH` [`00bbabb0`](#insn-00bbabb0) → [`00bbabb4`](#insn-00bbabb4)
- ブロック [`00bbabb4`](#insn-00bbabb4) 範囲 `[['00bbabb4', '00bbabb7']]`
  - `FALL_THROUGH` [`00bbabb4`](#insn-00bbabb4) → [`00bbabb8`](#insn-00bbabb8)
- ブロック [`00bbabb8`](#insn-00bbabb8) 範囲 `[['00bbabb8', '00bbabbb']]`
  - `FALL_THROUGH` [`00bbabb8`](#insn-00bbabb8) → [`00bbabbc`](#insn-00bbabbc)
- ブロック [`00bbabbc`](#insn-00bbabbc) 範囲 `[['00bbabbc', '00bbabbf']]`
- ブロック [`00bbabc0`](#insn-00bbabc0) 範囲 `[['00bbabc0', '00bbabc3']]`
  - `FALL_THROUGH` [`00bbabc0`](#insn-00bbabc0) → [`00bbabc4`](#insn-00bbabc4)
- ブロック [`00bbabc4`](#insn-00bbabc4) 範囲 `[['00bbabc4', '00bbabc7']]`
  - `FALL_THROUGH` [`00bbabc4`](#insn-00bbabc4) → [`00bbabc8`](#insn-00bbabc8)
- ブロック [`00bbabc8`](#insn-00bbabc8) 範囲 `[['00bbabc8', '00bbabcb']]`
  - `FALL_THROUGH` [`00bbabc8`](#insn-00bbabc8) → [`00bbabcc`](#insn-00bbabcc)
- ブロック [`00bbabcc`](#insn-00bbabcc) 範囲 `[['00bbabcc', '00bbabcf']]`
  - `FALL_THROUGH` [`00bbabcc`](#insn-00bbabcc) → [`00bbabd0`](#insn-00bbabd0)
- ブロック [`00bbabd0`](#insn-00bbabd0) 範囲 `[['00bbabd0', '00bbabd3']]`
  - `FALL_THROUGH` [`00bbabd0`](#insn-00bbabd0) → [`00bbabd4`](#insn-00bbabd4)
- ブロック [`00bbabd4`](#insn-00bbabd4) 範囲 `[['00bbabd4', '00bbabd7']]`

## 命令位置別の参照

- [`00bbaab8`](#insn-00bbaab8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaabc`](#insn-00bbaabc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaac0`](#insn-00bbaac0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaac8`](#insn-00bbaac8) → [`00be1de0`](../00be1/00be1de0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1de0` · 推定シンボル `None` · 推定型 `None`
- [`00bbaacc`](#insn-00bbaacc) → [`00bbaad8`](#insn-00bbaad8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaad4`](#insn-00bbaad4) → [`00bbaae4`](#insn-00bbaae4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaadc`](#insn-00bbaadc) → `002b0981`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbaae0`](#insn-00bbaae0) → [`00bbb19c`](../00bbb/00bbb19c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbb19c` · 推定シンボル `None` · 推定型 `None`
- [`00bbaae8`](#insn-00bbaae8) → [`00bd4fe4`](../00bd4/00bd4fe4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd4fe4` · 推定シンボル `None` · 推定型 `None`
- [`00bbaaec`](#insn-00bbaaec) → [`00bbab18`](#insn-00bbab18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaaf4`](#insn-00bbaaf4) → [`00bd4fd8`](../00bd4/00bd4fd8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd4fd8` · 推定シンボル `None` · 推定型 `None`
- [`00bbab0c`](#insn-00bbab0c) → [`00bbab2c`](#insn-00bbab2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbab14`](#insn-00bbab14) → [`00bbab30`](#insn-00bbab30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbab20`](#insn-00bbab20) → `002a02d6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbab24`](#insn-00bbab24) → `00c249a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbab24`](#insn-00bbab24) → `002999fd`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbab28`](#insn-00bbab28) → [`00bbb19c`](../00bbb/00bbb19c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbb19c` · 推定シンボル `None` · 推定型 `None`
- [`00bbab40`](#insn-00bbab40) → `Stack[-0x18]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbab4c`](#insn-00bbab4c) → [`00be1e30`](../00be1/00be1e30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1e30` · 推定シンボル `None` · 推定型 `None`
- [`00bbab60`](#insn-00bbab60) → `00c1ae88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbab70`](#insn-00bbab70) → `00c168a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTISt9exception` · 推定型 `pointer __((offset(0x10)))`
- [`00bbab78`](#insn-00bbab78) → `00c17600`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`
- [`00bbab80`](#insn-00bbab80) → `00c168a0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTISt9exception` · 推定型 `pointer __((offset(0x10)))`
- [`00bbab88`](#insn-00bbab88) → [`00bbb4c0`](../00bbb/00bbb4c0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00bbb4c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbab8c`](#insn-00bbab8c) → [`00bbabc0`](#insn-00bbabc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbab90`](#insn-00bbab90) → `Stack[-0x18]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbab98`](#insn-00bbab98) → `00c249a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbabb0`](#insn-00bbabb0) → `002a9148`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbabb4`](#insn-00bbabb4) → `002999fd`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbabbc`](#insn-00bbabbc) → [`00bbb19c`](../00bbb/00bbb19c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbb19c` · 推定シンボル `None` · 推定型 `None`
- [`00bbabc4`](#insn-00bbabc4) → `00c249a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbabc4`](#insn-00bbabc4) → `002999fd`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbabcc`](#insn-00bbabcc) → `0029c2dd`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbabd4`](#insn-00bbabd4) → [`00bbb19c`](../00bbb/00bbb19c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbb19c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbaab8`](#insn-00bbaab8)

~~~json
{
  "source": "00bbaab8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaabc`](#insn-00bbaabc)

~~~json
{
  "source": "00bbaabc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaac0`](#insn-00bbaac0)

~~~json
{
  "source": "00bbaac0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaac8`](#insn-00bbaac8)

~~~json
{
  "source": "00bbaac8",
  "target": "00be1de0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaacc`](#insn-00bbaacc)

~~~json
{
  "source": "00bbaacc",
  "target": "00bbaad8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaad4`](#insn-00bbaad4)

~~~json
{
  "source": "00bbaad4",
  "target": "00bbaae4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaadc`](#insn-00bbaadc)

~~~json
{
  "source": "00bbaadc",
  "target": "002b0981",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b0981",
  "offset": 0,
  "size": 12,
  "datatype": "string",
  "bytes": "7465726d696e6174696e6700",
  "capture_start": "002b0981",
  "capture_bytes": 12,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbaae0`](#insn-00bbaae0)

~~~json
{
  "source": "00bbaae0",
  "target": "00bbb19c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaae8`](#insn-00bbaae8)

~~~json
{
  "source": "00bbaae8",
  "target": "00bd4fe4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaaec`](#insn-00bbaaec)

~~~json
{
  "source": "00bbaaec",
  "target": "00bbab18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaaf4`](#insn-00bbaaf4)

~~~json
{
  "source": "00bbaaf4",
  "target": "00bd4fd8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbab0c`](#insn-00bbab0c)

~~~json
{
  "source": "00bbab0c",
  "target": "00bbab2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbab14`](#insn-00bbab14)

~~~json
{
  "source": "00bbab14",
  "target": "00bbab30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbab20`](#insn-00bbab20)

~~~json
{
  "source": "00bbab20",
  "target": "002a02d6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a02d6",
  "offset": 0,
  "size": 40,
  "datatype": "string",
  "bytes": "7465726d696e6174696e672064756520746f20257320666f726569676e206578",
  "capture_start": "002a02d6",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bbab24`](#insn-00bbab24)

~~~json
{
  "source": "00bbab24",
  "target": "00c249a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c249a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbab24`](#insn-00bbab24)

~~~json
{
  "source": "00bbab24",
  "target": "002999fd",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002999fd",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "756e63617567687400",
  "capture_start": "002999fd",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbab28`](#insn-00bbab28)

~~~json
{
  "source": "00bbab28",
  "target": "00bbb19c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbab40`](#insn-00bbab40)

~~~json
{
  "source": "00bbab40",
  "target": "Stack[-0x18]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbab4c`](#insn-00bbab4c)

~~~json
{
  "source": "00bbab4c",
  "target": "00be1e30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbab60`](#insn-00bbab60)

~~~json
{
  "source": "00bbab60",
  "target": "00c1ae88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ae88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbab70`](#insn-00bbab70)

~~~json
{
  "source": "00bbab70",
  "target": "00c168a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c168a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbab78`](#insn-00bbab78)

~~~json
{
  "source": "00bbab78",
  "target": "00c17600",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c175d0",
  "offset": 48,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bbab80`](#insn-00bbab80)

~~~json
{
  "source": "00bbab80",
  "target": "00c168a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c168a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbab88`](#insn-00bbab88)

~~~json
{
  "source": "00bbab88",
  "target": "00bbb4c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbab8c`](#insn-00bbab8c)

~~~json
{
  "source": "00bbab8c",
  "target": "00bbabc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbab90`](#insn-00bbab90)

~~~json
{
  "source": "00bbab90",
  "target": "Stack[-0x18]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbab98`](#insn-00bbab98)

~~~json
{
  "source": "00bbab98",
  "target": "00c249a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c249a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbabb0`](#insn-00bbabb0)

~~~json
{
  "source": "00bbabb0",
  "target": "002a9148",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a9148",
  "offset": 0,
  "size": 47,
  "datatype": "string",
  "bytes": "7465726d696e6174696e672064756520746f20257320657863657074696f6e20",
  "capture_start": "002a9148",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bbabb4`](#insn-00bbabb4)

~~~json
{
  "source": "00bbabb4",
  "target": "002999fd",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002999fd",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "756e63617567687400",
  "capture_start": "002999fd",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbabbc`](#insn-00bbabbc)

~~~json
{
  "source": "00bbabbc",
  "target": "00bbb19c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbabc4`](#insn-00bbabc4)

~~~json
{
  "source": "00bbabc4",
  "target": "00c249a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c249a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbabc4`](#insn-00bbabc4)

~~~json
{
  "source": "00bbabc4",
  "target": "002999fd",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002999fd",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "756e63617567687400",
  "capture_start": "002999fd",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbabcc`](#insn-00bbabcc)

~~~json
{
  "source": "00bbabcc",
  "target": "0029c2dd",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029c2dd",
  "offset": 0,
  "size": 43,
  "datatype": "string",
  "bytes": "7465726d696e6174696e672064756520746f20257320657863657074696f6e20",
  "capture_start": "0029c2dd",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bbabd4`](#insn-00bbabd4)

~~~json
{
  "source": "00bbabd4",
  "target": "00bbb19c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
