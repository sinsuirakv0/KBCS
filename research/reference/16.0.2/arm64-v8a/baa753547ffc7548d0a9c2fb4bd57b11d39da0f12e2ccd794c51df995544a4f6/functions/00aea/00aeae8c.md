# 00aeae8c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aeadf0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aea/00aeadf0.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0065.md#compare-e1b0fcc73a843cf0ffcd73fe04a10d4d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00aebe80`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aeb/00aebe80.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-f1690b671a0dbf10bcc52adef77114dc)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeae8c",
  "name": "FUN_00aeae8c",
  "size": 368,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f9e30ac2e79a38df647a0d0f704a993fabfad68e7bc31eed196c724a92594b88",
  "source_text_sha256": "f9e30ac2e79a38df647a0d0f704a993fabfad68e7bc31eed196c724a92594b88",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeae8c",
        "00aeaff7"
      ],
      [
        "00aeb02c",
        "00aeb02f"
      ]
    ],
    "bytes_sha256": "adc32438f232c4d9a96482bf4e8b34c0cda0541979298fe8fde31161c95eca82",
    "instruction_count": 92,
    "instruction_bytes": 368,
    "body_bytes": 368,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00acecc4](../00ace/00acecc4.md)
- [00acee90](../00ace/00acee90.md)
- [00acf228](../00acf/00acf228.md)

## 呼び出し先

- [00470880](../00470/00470880.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c580d0](../00c58/00c580d0.md)
- [00c58520](../00c58/00c58520.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4873 bytes

~~~c

int FUN_00aeae8c(long param_1,int param_2)

{
  void *__src;
  size_t __n;
  long lVar1;
  long *plVar2;
  bool bVar3;
  wchar_t *__s;
  wchar_t *pwVar4;
  int iVar5;
  wchar_t *pwVar6;
  long *plVar7;
  long *plVar8;
  undefined8 local_80;
  undefined8 local_78;
  undefined8 uStack_70;
  long local_68;
  
  lVar1 = tpidr_el0;
  local_68 = *(long *)(lVar1 + 0x28);
  plVar7 = *(long **)(param_1 + 0x33c0);
  if (plVar7 == (long *)(param_1 + 0x33c8)) {
    iVar5 = -1;
                    /* catch() { ... } // from try @ 00aeabe4 with catch @ 00aeaf9c */
  }
  else {
    do {
      __src = (void *)plVar7[5];
      iVar5 = (int)(short)plVar7[4];
      local_78 = 0;
      uStack_70 = 0;
                    /* try { // try from 00aeaf00 to 00beaf03 has its CatchHandler @ 00aeaf28 */
      __n = plVar7[6] - (long)__src;
      local_80 = 0;
      if (__n == 0) {
        pwVar6 = (wchar_t *)0x0;
        __s = (wchar_t *)0x0;
      }
      else {
        if ((long)__n < 0) {
          if (*(long *)(lVar1 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
            FUN_00470880(&local_80);
          }
          goto LAB_00aeb02c;
        }
                    /* try { // try from 00aeaf14 to 00beaf17 has its CatchHandler @ 00aeaf20 */
        __s = (wchar_t *)_Znwm(__n);
                    /* catch() { ... } // from try @ 00aead68 with catch @ 00aeaf18
                       try { // try from 00aeaf18 to 00beafd7 has its CatchHandler @ 00aea9c8 */
                    /* catch() { ... } // from try @ 00aeacfc with catch @ 00aeaf1c */
                    /* catch() { ... } // from try @ 00aeadb4 with catch @ 00aeaf20
                       catch() { ... } // from try @ 00aeaf14 with catch @ 00aeaf20 */
                    /* catch() { ... } // from try @ 00aeab14 with catch @ 00aeaf24 */
        pwVar6 = (wchar_t *)((long)__s + __n);
                    /* catch() { ... } // from try @ 00aead48 with catch @ 00aeaf28
                       catch() { ... } // from try @ 00aeaf00 with catch @ 00aeaf28 */
        memcpy(__s,__src,__n);
      }
                    /* catch() { ... } // from try @ 00aeaadc with catch @ 00aeaf40 */
                    /* catch() { ... } // from try @ 00aeaa90 with catch @ 00aeaf44 */
      pwVar4 = wmemchr(__s,param_2 + L'\xc4653600',(long)pwVar6 - (long)__s >> 2);
                    /* catch() { ... } // from try @ 00aeaa84 with catch @ 00aeaf54 */
      if (__s != (wchar_t *)0x0) {
        _ZdlPv(__s);
      }
                    /* catch() { ... } // from try @ 00aeac8c with catch @ 00aeaf64 */
      if (pwVar4 != (wchar_t *)0x0 && pwVar4 != pwVar6) goto LAB_00aeafa8;
                    /* catch() { ... } // from try @ 00aeaa74 with catch @ 00aeaf68 */
      plVar2 = (long *)plVar7[1];
      plVar8 = plVar7;
      if ((long *)plVar7[1] == (long *)0x0) {
        do {
          plVar7 = (long *)plVar8[2];
          bVar3 = (long *)*plVar7 != plVar8;
          plVar8 = plVar7;
                    /* catch() { ... } // from try @ 00aeaa14 with catch @ 00aeaf90 */
        } while (bVar3);
      }
      else {
        do {
                    /* catch() { ... } // from try @ 00aeacd8 with catch @ 00aeaf70
                       catch() { ... } // from try @ 00aeaeec with catch @ 00aeaf70 */
          plVar7 = plVar2;
                    /* catch() { ... } // from try @ 00aeaa48 with catch @ 00aeaf74 */
          plVar2 = (long *)*plVar7;
        } while ((long *)*plVar7 != (long *)0x0);
      }
                    /* try { // try from 00aeaeec to 00beaeef has its CatchHandler @ 00aeaf70 */
    } while (plVar7 != (long *)(param_1 + 0x33c8));
                    /* catch() { ... } // from try @ 00aeac44 with catch @ 00aeafa0 */
    iVar5 = -1;
  }
LAB_00aeafa8:
  if (*(long *)(lVar1 + 0x28) == local_68) {
                    /* catch() { ... } // from try @ 00aeb27c with catch @ 00aeafd8
                       catch() { ... } // from try @ 00aeb388 with catch @ 00aeafd8
                       catch() { ... } // from try @ 00aeb55c with catch @ 00aeafd8
                       catch() { ... } // from try @ 00aeb5ec with catch @ 00aeafd8
                       catch() { ... } // from try @ 00aeb680 with catch @ 00aeafd8
                       catch() { ... } // from try @ 00aeb710 with catch @ 00aeafd8
                       catch() { ... } // from try @ 00aeb8e4 with catch @ 00aeafd8
                       catch() { ... } // from try @ 00aeb92c with catch @ 00aeafd8
                       catch() { ... } // from try @ 00aebbc4 with catch @ 00aeafd8
                       catch() { ... } // from try @ 00aebc60 with catch @ 00aeafd8
                       catch() { ... } // from try @ 00aebe5c with catch @ 00aeafd8 */
    return iVar5;
  }
LAB_00aeb02c:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeae8c"></a> `00aeae8c` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00aeae90"></a> `00aeae90` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aeae94"></a> `00aeae94` | `fc 6f 04 a9` | stp x28,x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aeae98"></a> `00aeae98` | `fa 67 05 a9` | stp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aeae9c"></a> `00aeae9c` | `f8 5f 06 a9` | stp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aeaea0"></a> `00aeaea0` | `f6 57 07 a9` | stp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aeaea4"></a> `00aeaea4` | `f4 4f 08 a9` | stp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aeaea8"></a> `00aeaea8` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aeaeac"></a> `00aeaeac` | `49 d0 3b d5` | mrs x9,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aeaeb0"></a> `00aeaeb0` | `28 15 40 f9` | ldr x8,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00aeaeb4"></a> `00aeaeb4` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeaeb8"></a> `00aeaeb8` | `08 79 86 52` | mov w8,#0x33c8 | `FALL_THROUGH`
<a id="insn-00aeaebc"></a> `00aeaebc` | `1c e0 59 f9` | ldr x28,[x0, #0x33c0] | `FALL_THROUGH`
<a id="insn-00aeaec0"></a> `00aeaec0` | `1a 00 08 8b` | add x26,x0,x8 | `FALL_THROUGH`
<a id="insn-00aeaec4"></a> `00aeaec4` | `9f 03 1a eb` | cmp x28,x26 | `FALL_THROUGH`
<a id="insn-00aeaec8"></a> `00aeaec8` | `80 06 00 54` | b.eq 0x00aeaf98 | `CONDITIONAL_JUMP`
<a id="insn-00aeaecc"></a> `00aeaecc` | `1b c0 86 52` | mov w27,#0x3600 | `FALL_THROUGH`
<a id="insn-00aeaed0"></a> `00aeaed0` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00aeaed4"></a> `00aeaed4` | `f9 23 00 91` | add x25,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aeaed8"></a> `00aeaed8` | `bb 8c b8 72` | movk w27,#0xc465, LSL #16 | `FALL_THROUGH`
<a id="insn-00aeaedc"></a> `00aeaedc` | `e9 03 00 f9` | str x9,[sp] | `FALL_THROUGH`
<a id="insn-00aeaee0"></a> `00aeaee0` | `04 00 00 14` | b 0x00aeaef0 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeaee4"></a> `00aeaee4` | `1f 01 1a eb` | cmp x8,x26 | `FALL_THROUGH`
<a id="insn-00aeaee8"></a> `00aeaee8` | `fc 03 08 aa` | mov x28,x8 | `FALL_THROUGH`
<a id="insn-00aeaeec"></a> `00aeaeec` | `a0 05 00 54` | b.eq 0x00aeafa0 | `CONDITIONAL_JUMP`
<a id="insn-00aeaef0"></a> `00aeaef0` | `96 a3 42 a9` | ldp x22,x8,[x28, #0x28] | `FALL_THROUGH`
<a id="insn-00aeaef4"></a> `00aeaef4` | `94 43 c0 79` | ldrsh w20,[x28, #0x20] | `FALL_THROUGH`
<a id="insn-00aeaef8"></a> `00aeaef8` | `3f 7f 01 a9` | stp xzr,xzr,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00aeaefc"></a> `00aeaefc` | `f4 13 00 79` | strh w20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aeaf00"></a> `00aeaf00` | `17 01 16 eb` | subs x23,x8,x22 | `FALL_THROUGH`
<a id="insn-00aeaf04"></a> `00aeaf04` | `3f 83 00 f8` | stur xzr,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00aeaf08"></a> `00aeaf08` | `40 01 00 54` | b.eq 0x00aeaf30 | `CONDITIONAL_JUMP`
<a id="insn-00aeaf0c"></a> `00aeaf0c` | `97 06 f8 b7` | tbnz x23,#0x3f,0x00aeafdc | `CONDITIONAL_JUMP`
<a id="insn-00aeaf10"></a> `00aeaf10` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00aeaf14"></a> `00aeaf14` | `13 b4 05 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00aeaf18"></a> `00aeaf18` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00aeaf1c"></a> `00aeaf1c` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00aeaf20"></a> `00aeaf20` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00aeaf24"></a> `00aeaf24` | `18 00 17 8b` | add x24,x0,x23 | `FALL_THROUGH`
<a id="insn-00aeaf28"></a> `00aeaf28` | `6a b4 05 94` | bl 0x00c580d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aeaf2c"></a> `00aeaf2c` | `03 00 00 14` | b 0x00aeaf38 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeaf30"></a> `00aeaf30` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-00aeaf34"></a> `00aeaf34` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00aeaf38"></a> `00aeaf38` | `08 03 15 cb` | sub x8,x24,x21 | `FALL_THROUGH`
<a id="insn-00aeaf3c"></a> `00aeaf3c` | `61 02 1b 0b` | add w1,w19,w27 | `FALL_THROUGH`
<a id="insn-00aeaf40"></a> `00aeaf40` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aeaf44"></a> `00aeaf44` | `02 fd 42 93` | asr x2,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00aeaf48"></a> `00aeaf48` | `76 b5 05 94` | bl 0x00c58520 | `UNCONDITIONAL_CALL`
<a id="insn-00aeaf4c"></a> `00aeaf4c` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-00aeaf50"></a> `00aeaf50` | `04 10 58 fa` | ccmp x0,x24,#0x4,ne | `FALL_THROUGH`
<a id="insn-00aeaf54"></a> `00aeaf54` | `f6 17 9f 1a` | cset w22,eq | `FALL_THROUGH`
<a id="insn-00aeaf58"></a> `00aeaf58` | `75 00 00 b4` | cbz x21,0x00aeaf64 | `CONDITIONAL_JUMP`
<a id="insn-00aeaf5c"></a> `00aeaf5c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aeaf60"></a> `00aeaf60` | `08 b4 05 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00aeaf64"></a> `00aeaf64` | `16 02 00 34` | cbz w22,0x00aeafa4 | `CONDITIONAL_JUMP`
<a id="insn-00aeaf68"></a> `00aeaf68` | `89 07 40 f9` | ldr x9,[x28, #0x8] | `FALL_THROUGH`
<a id="insn-00aeaf6c"></a> `00aeaf6c` | `a9 00 00 b4` | cbz x9,0x00aeaf80 | `CONDITIONAL_JUMP`
<a id="insn-00aeaf70"></a> `00aeaf70` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00aeaf74"></a> `00aeaf74` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00aeaf78"></a> `00aeaf78` | `c9 ff ff b5` | cbnz x9,0x00aeaf70 | `CONDITIONAL_JUMP`
<a id="insn-00aeaf7c"></a> `00aeaf7c` | `da ff ff 17` | b 0x00aeaee4 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeaf80"></a> `00aeaf80` | `88 0b 40 f9` | ldr x8,[x28, #0x10] | `FALL_THROUGH`
<a id="insn-00aeaf84"></a> `00aeaf84` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00aeaf88"></a> `00aeaf88` | `3f 01 1c eb` | cmp x9,x28 | `FALL_THROUGH`
<a id="insn-00aeaf8c"></a> `00aeaf8c` | `fc 03 08 aa` | mov x28,x8 | `FALL_THROUGH`
<a id="insn-00aeaf90"></a> `00aeaf90` | `81 ff ff 54` | b.ne 0x00aeaf80 | `CONDITIONAL_JUMP`
<a id="insn-00aeaf94"></a> `00aeaf94` | `d4 ff ff 17` | b 0x00aeaee4 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeaf98"></a> `00aeaf98` | `14 00 80 12` | mov w20,#0xffffffff | `FALL_THROUGH`
<a id="insn-00aeaf9c"></a> `00aeaf9c` | `03 00 00 14` | b 0x00aeafa8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeafa0"></a> `00aeafa0` | `14 00 80 12` | mov w20,#0xffffffff | `FALL_THROUGH`
<a id="insn-00aeafa4"></a> `00aeafa4` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00aeafa8"></a> `00aeafa8` | `28 15 40 f9` | ldr x8,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00aeafac"></a> `00aeafac` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeafb0"></a> `00aeafb0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aeafb4"></a> `00aeafb4` | `c1 03 00 54` | b.ne 0x00aeb02c | `CONDITIONAL_JUMP`
<a id="insn-00aeafb8"></a> `00aeafb8` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00aeafbc"></a> `00aeafbc` | `f4 4f 48 a9` | ldp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aeafc0"></a> `00aeafc0` | `f6 57 47 a9` | ldp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aeafc4"></a> `00aeafc4` | `f8 5f 46 a9` | ldp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aeafc8"></a> `00aeafc8` | `fa 67 45 a9` | ldp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aeafcc"></a> `00aeafcc` | `fc 6f 44 a9` | ldp x28,x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aeafd0"></a> `00aeafd0` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aeafd4"></a> `00aeafd4` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00aeafd8"></a> `00aeafd8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aeafdc"></a> `00aeafdc` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00aeafe0"></a> `00aeafe0` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aeafe4"></a> `00aeafe4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeafe8"></a> `00aeafe8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aeafec"></a> `00aeafec` | `01 02 00 54` | b.ne 0x00aeb02c | `CONDITIONAL_JUMP`
<a id="insn-00aeaff0"></a> `00aeaff0` | `20 23 00 91` | add x0,x25,#0x8 | `FALL_THROUGH`
<a id="insn-00aeaff4"></a> `00aeaff4` | `23 16 e6 97` | bl 0x00470880 | `CALL_TERMINATOR`
<a id="insn-00aeb02c"></a> `00aeb02c` | `e1 b3 05 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeae8c`](#insn-00aeae8c) 範囲 `[['00aeae8c', '00aeaecb']]`
  - `CONDITIONAL_JUMP` [`00aeaec8`](#insn-00aeaec8) → [`00aeaf98`](#insn-00aeaf98)
  - `FALL_THROUGH` [`00aeaec8`](#insn-00aeaec8) → [`00aeaecc`](#insn-00aeaecc)
- ブロック [`00aeaecc`](#insn-00aeaecc) 範囲 `[['00aeaecc', '00aeaee3']]`
  - `UNCONDITIONAL_JUMP` [`00aeaee0`](#insn-00aeaee0) → [`00aeaef0`](#insn-00aeaef0)
- ブロック [`00aeaee4`](#insn-00aeaee4) 範囲 `[['00aeaee4', '00aeaeeb']]`
  - `FALL_THROUGH` [`00aeaee8`](#insn-00aeaee8) → [`00aeaeec`](#insn-00aeaeec)
- ブロック [`00aeaeec`](#insn-00aeaeec) 範囲 `[['00aeaeec', '00aeaeef']]`
  - `CONDITIONAL_JUMP` [`00aeaeec`](#insn-00aeaeec) → [`00aeafa0`](#insn-00aeafa0)
  - `FALL_THROUGH` [`00aeaeec`](#insn-00aeaeec) → [`00aeaef0`](#insn-00aeaef0)
- ブロック [`00aeaef0`](#insn-00aeaef0) 範囲 `[['00aeaef0', '00aeaeff']]`
  - `FALL_THROUGH` [`00aeaefc`](#insn-00aeaefc) → [`00aeaf00`](#insn-00aeaf00)
- ブロック [`00aeaf00`](#insn-00aeaf00) 範囲 `[['00aeaf00', '00aeaf0b']]`
  - `CONDITIONAL_JUMP` [`00aeaf08`](#insn-00aeaf08) → [`00aeaf30`](#insn-00aeaf30)
  - `FALL_THROUGH` [`00aeaf08`](#insn-00aeaf08) → [`00aeaf0c`](#insn-00aeaf0c)
- ブロック [`00aeaf0c`](#insn-00aeaf0c) 範囲 `[['00aeaf0c', '00aeaf0f']]`
  - `CONDITIONAL_JUMP` [`00aeaf0c`](#insn-00aeaf0c) → [`00aeafdc`](#insn-00aeafdc)
  - `FALL_THROUGH` [`00aeaf0c`](#insn-00aeaf0c) → [`00aeaf10`](#insn-00aeaf10)
- ブロック [`00aeaf10`](#insn-00aeaf10) 範囲 `[['00aeaf10', '00aeaf13']]`
  - `FALL_THROUGH` [`00aeaf10`](#insn-00aeaf10) → [`00aeaf14`](#insn-00aeaf14)
- ブロック [`00aeaf14`](#insn-00aeaf14) 範囲 `[['00aeaf14', '00aeaf17']]`
  - `FALL_THROUGH` [`00aeaf14`](#insn-00aeaf14) → [`00aeaf18`](#insn-00aeaf18)
- ブロック [`00aeaf18`](#insn-00aeaf18) 範囲 `[['00aeaf18', '00aeaf1b']]`
  - `FALL_THROUGH` [`00aeaf18`](#insn-00aeaf18) → [`00aeaf1c`](#insn-00aeaf1c)
- ブロック [`00aeaf1c`](#insn-00aeaf1c) 範囲 `[['00aeaf1c', '00aeaf1f']]`
  - `FALL_THROUGH` [`00aeaf1c`](#insn-00aeaf1c) → [`00aeaf20`](#insn-00aeaf20)
- ブロック [`00aeaf20`](#insn-00aeaf20) 範囲 `[['00aeaf20', '00aeaf23']]`
  - `FALL_THROUGH` [`00aeaf20`](#insn-00aeaf20) → [`00aeaf24`](#insn-00aeaf24)
- ブロック [`00aeaf24`](#insn-00aeaf24) 範囲 `[['00aeaf24', '00aeaf27']]`
  - `FALL_THROUGH` [`00aeaf24`](#insn-00aeaf24) → [`00aeaf28`](#insn-00aeaf28)
- ブロック [`00aeaf28`](#insn-00aeaf28) 範囲 `[['00aeaf28', '00aeaf2f']]`
  - `UNCONDITIONAL_JUMP` [`00aeaf2c`](#insn-00aeaf2c) → [`00aeaf38`](#insn-00aeaf38)
- ブロック [`00aeaf30`](#insn-00aeaf30) 範囲 `[['00aeaf30', '00aeaf37']]`
  - `FALL_THROUGH` [`00aeaf34`](#insn-00aeaf34) → [`00aeaf38`](#insn-00aeaf38)
- ブロック [`00aeaf38`](#insn-00aeaf38) 範囲 `[['00aeaf38', '00aeaf3f']]`
  - `FALL_THROUGH` [`00aeaf3c`](#insn-00aeaf3c) → [`00aeaf40`](#insn-00aeaf40)
- ブロック [`00aeaf40`](#insn-00aeaf40) 範囲 `[['00aeaf40', '00aeaf43']]`
  - `FALL_THROUGH` [`00aeaf40`](#insn-00aeaf40) → [`00aeaf44`](#insn-00aeaf44)
- ブロック [`00aeaf44`](#insn-00aeaf44) 範囲 `[['00aeaf44', '00aeaf53']]`
  - `FALL_THROUGH` [`00aeaf50`](#insn-00aeaf50) → [`00aeaf54`](#insn-00aeaf54)
- ブロック [`00aeaf54`](#insn-00aeaf54) 範囲 `[['00aeaf54', '00aeaf5b']]`
  - `CONDITIONAL_JUMP` [`00aeaf58`](#insn-00aeaf58) → [`00aeaf64`](#insn-00aeaf64)
  - `FALL_THROUGH` [`00aeaf58`](#insn-00aeaf58) → [`00aeaf5c`](#insn-00aeaf5c)
- ブロック [`00aeaf5c`](#insn-00aeaf5c) 範囲 `[['00aeaf5c', '00aeaf63']]`
  - `FALL_THROUGH` [`00aeaf60`](#insn-00aeaf60) → [`00aeaf64`](#insn-00aeaf64)
- ブロック [`00aeaf64`](#insn-00aeaf64) 範囲 `[['00aeaf64', '00aeaf67']]`
  - `CONDITIONAL_JUMP` [`00aeaf64`](#insn-00aeaf64) → [`00aeafa4`](#insn-00aeafa4)
  - `FALL_THROUGH` [`00aeaf64`](#insn-00aeaf64) → [`00aeaf68`](#insn-00aeaf68)
- ブロック [`00aeaf68`](#insn-00aeaf68) 範囲 `[['00aeaf68', '00aeaf6f']]`
  - `CONDITIONAL_JUMP` [`00aeaf6c`](#insn-00aeaf6c) → [`00aeaf80`](#insn-00aeaf80)
  - `FALL_THROUGH` [`00aeaf6c`](#insn-00aeaf6c) → [`00aeaf70`](#insn-00aeaf70)
- ブロック [`00aeaf70`](#insn-00aeaf70) 範囲 `[['00aeaf70', '00aeaf73']]`
  - `FALL_THROUGH` [`00aeaf70`](#insn-00aeaf70) → [`00aeaf74`](#insn-00aeaf74)
- ブロック [`00aeaf74`](#insn-00aeaf74) 範囲 `[['00aeaf74', '00aeaf7b']]`
  - `CONDITIONAL_JUMP` [`00aeaf78`](#insn-00aeaf78) → [`00aeaf70`](#insn-00aeaf70)
  - `FALL_THROUGH` [`00aeaf78`](#insn-00aeaf78) → [`00aeaf7c`](#insn-00aeaf7c)
- ブロック [`00aeaf7c`](#insn-00aeaf7c) 範囲 `[['00aeaf7c', '00aeaf7f']]`
  - `UNCONDITIONAL_JUMP` [`00aeaf7c`](#insn-00aeaf7c) → [`00aeaee4`](#insn-00aeaee4)
- ブロック [`00aeaf80`](#insn-00aeaf80) 範囲 `[['00aeaf80', '00aeaf8f']]`
  - `FALL_THROUGH` [`00aeaf8c`](#insn-00aeaf8c) → [`00aeaf90`](#insn-00aeaf90)
- ブロック [`00aeaf90`](#insn-00aeaf90) 範囲 `[['00aeaf90', '00aeaf93']]`
  - `CONDITIONAL_JUMP` [`00aeaf90`](#insn-00aeaf90) → [`00aeaf80`](#insn-00aeaf80)
  - `FALL_THROUGH` [`00aeaf90`](#insn-00aeaf90) → [`00aeaf94`](#insn-00aeaf94)
- ブロック [`00aeaf94`](#insn-00aeaf94) 範囲 `[['00aeaf94', '00aeaf97']]`
  - `UNCONDITIONAL_JUMP` [`00aeaf94`](#insn-00aeaf94) → [`00aeaee4`](#insn-00aeaee4)
- ブロック [`00aeaf98`](#insn-00aeaf98) 範囲 `[['00aeaf98', '00aeaf9b']]`
  - `FALL_THROUGH` [`00aeaf98`](#insn-00aeaf98) → [`00aeaf9c`](#insn-00aeaf9c)
- ブロック [`00aeaf9c`](#insn-00aeaf9c) 範囲 `[['00aeaf9c', '00aeaf9f']]`
  - `UNCONDITIONAL_JUMP` [`00aeaf9c`](#insn-00aeaf9c) → [`00aeafa8`](#insn-00aeafa8)
- ブロック [`00aeafa0`](#insn-00aeafa0) 範囲 `[['00aeafa0', '00aeafa3']]`
  - `FALL_THROUGH` [`00aeafa0`](#insn-00aeafa0) → [`00aeafa4`](#insn-00aeafa4)
- ブロック [`00aeafa4`](#insn-00aeafa4) 範囲 `[['00aeafa4', '00aeafa7']]`
  - `FALL_THROUGH` [`00aeafa4`](#insn-00aeafa4) → [`00aeafa8`](#insn-00aeafa8)
- ブロック [`00aeafa8`](#insn-00aeafa8) 範囲 `[['00aeafa8', '00aeafb7']]`
  - `CONDITIONAL_JUMP` [`00aeafb4`](#insn-00aeafb4) → [`00aeb02c`](#insn-00aeb02c)
  - `FALL_THROUGH` [`00aeafb4`](#insn-00aeafb4) → [`00aeafb8`](#insn-00aeafb8)
- ブロック [`00aeafb8`](#insn-00aeafb8) 範囲 `[['00aeafb8', '00aeafd7']]`
  - `FALL_THROUGH` [`00aeafd4`](#insn-00aeafd4) → [`00aeafd8`](#insn-00aeafd8)
- ブロック [`00aeafd8`](#insn-00aeafd8) 範囲 `[['00aeafd8', '00aeafdb']]`
- ブロック [`00aeafdc`](#insn-00aeafdc) 範囲 `[['00aeafdc', '00aeafef']]`
  - `CONDITIONAL_JUMP` [`00aeafec`](#insn-00aeafec) → [`00aeb02c`](#insn-00aeb02c)
  - `FALL_THROUGH` [`00aeafec`](#insn-00aeafec) → [`00aeaff0`](#insn-00aeaff0)
- ブロック [`00aeaff0`](#insn-00aeaff0) 範囲 `[['00aeaff0', '00aeaff7']]`
- ブロック [`00aeb02c`](#insn-00aeb02c) 範囲 `[['00aeb02c', '00aeb02f']]`

## 命令位置別の参照

- [`00aeae90`](#insn-00aeae90) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae94`](#insn-00aeae94) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae98`](#insn-00aeae98) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae9c`](#insn-00aeae9c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaea0`](#insn-00aeaea0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaea4`](#insn-00aeaea4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaeb4`](#insn-00aeaeb4) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaec8`](#insn-00aeaec8) → [`00aeaf98`](#insn-00aeaf98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaedc`](#insn-00aeaedc) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaee0`](#insn-00aeaee0) → [`00aeaef0`](#insn-00aeaef0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaeec`](#insn-00aeaeec) → [`00aeafa0`](#insn-00aeafa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaef8`](#insn-00aeaef8) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaefc`](#insn-00aeaefc) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf04`](#insn-00aeaf04) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf08`](#insn-00aeaf08) → [`00aeaf30`](#insn-00aeaf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf0c`](#insn-00aeaf0c) → [`00aeafdc`](#insn-00aeafdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf14`](#insn-00aeaf14) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf28`](#insn-00aeaf28) → [`00c580d0`](../00c58/00c580d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580d0` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf2c`](#insn-00aeaf2c) → [`00aeaf38`](#insn-00aeaf38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf48`](#insn-00aeaf48) → [`00c58520`](../00c58/00c58520.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58520` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf58`](#insn-00aeaf58) → [`00aeaf64`](#insn-00aeaf64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf60`](#insn-00aeaf60) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf64`](#insn-00aeaf64) → [`00aeafa4`](#insn-00aeafa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf6c`](#insn-00aeaf6c) → [`00aeaf80`](#insn-00aeaf80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf78`](#insn-00aeaf78) → [`00aeaf70`](#insn-00aeaf70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf7c`](#insn-00aeaf7c) → [`00aeaee4`](#insn-00aeaee4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf90`](#insn-00aeaf90) → [`00aeaf80`](#insn-00aeaf80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf94`](#insn-00aeaf94) → [`00aeaee4`](#insn-00aeaee4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf9c`](#insn-00aeaf9c) → [`00aeafa8`](#insn-00aeafa8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeafa4`](#insn-00aeafa4) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeafac`](#insn-00aeafac) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeafb4`](#insn-00aeafb4) → [`00aeb02c`](#insn-00aeb02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeafbc`](#insn-00aeafbc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeafc0`](#insn-00aeafc0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeafc4`](#insn-00aeafc4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeafc8`](#insn-00aeafc8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeafcc`](#insn-00aeafcc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeafd0`](#insn-00aeafd0) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeafdc`](#insn-00aeafdc) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeafe4`](#insn-00aeafe4) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeafec`](#insn-00aeafec) → [`00aeb02c`](#insn-00aeb02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaff4`](#insn-00aeaff4) → [`00470880`](../00470/00470880.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470880` · 推定シンボル `None` · 推定型 `None`
- [`00aeb02c`](#insn-00aeb02c) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeae90`](#insn-00aeae90)

~~~json
{
  "source": "00aeae90",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae94`](#insn-00aeae94)

~~~json
{
  "source": "00aeae94",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae98`](#insn-00aeae98)

~~~json
{
  "source": "00aeae98",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae9c`](#insn-00aeae9c)

~~~json
{
  "source": "00aeae9c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaea0`](#insn-00aeaea0)

~~~json
{
  "source": "00aeaea0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaea4`](#insn-00aeaea4)

~~~json
{
  "source": "00aeaea4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaeb4`](#insn-00aeaeb4)

~~~json
{
  "source": "00aeaeb4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaec8`](#insn-00aeaec8)

~~~json
{
  "source": "00aeaec8",
  "target": "00aeaf98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaedc`](#insn-00aeaedc)

~~~json
{
  "source": "00aeaedc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaee0`](#insn-00aeaee0)

~~~json
{
  "source": "00aeaee0",
  "target": "00aeaef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaeec`](#insn-00aeaeec)

~~~json
{
  "source": "00aeaeec",
  "target": "00aeafa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaef8`](#insn-00aeaef8)

~~~json
{
  "source": "00aeaef8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaefc`](#insn-00aeaefc)

~~~json
{
  "source": "00aeaefc",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf04`](#insn-00aeaf04)

~~~json
{
  "source": "00aeaf04",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf08`](#insn-00aeaf08)

~~~json
{
  "source": "00aeaf08",
  "target": "00aeaf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf0c`](#insn-00aeaf0c)

~~~json
{
  "source": "00aeaf0c",
  "target": "00aeafdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf14`](#insn-00aeaf14)

~~~json
{
  "source": "00aeaf14",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeaf28`](#insn-00aeaf28)

~~~json
{
  "source": "00aeaf28",
  "target": "00c580d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeaf2c`](#insn-00aeaf2c)

~~~json
{
  "source": "00aeaf2c",
  "target": "00aeaf38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf48`](#insn-00aeaf48)

~~~json
{
  "source": "00aeaf48",
  "target": "00c58520",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeaf58`](#insn-00aeaf58)

~~~json
{
  "source": "00aeaf58",
  "target": "00aeaf64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf60`](#insn-00aeaf60)

~~~json
{
  "source": "00aeaf60",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeaf64`](#insn-00aeaf64)

~~~json
{
  "source": "00aeaf64",
  "target": "00aeafa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf6c`](#insn-00aeaf6c)

~~~json
{
  "source": "00aeaf6c",
  "target": "00aeaf80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf78`](#insn-00aeaf78)

~~~json
{
  "source": "00aeaf78",
  "target": "00aeaf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf7c`](#insn-00aeaf7c)

~~~json
{
  "source": "00aeaf7c",
  "target": "00aeaee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf90`](#insn-00aeaf90)

~~~json
{
  "source": "00aeaf90",
  "target": "00aeaf80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf94`](#insn-00aeaf94)

~~~json
{
  "source": "00aeaf94",
  "target": "00aeaee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf9c`](#insn-00aeaf9c)

~~~json
{
  "source": "00aeaf9c",
  "target": "00aeafa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeafa4`](#insn-00aeafa4)

~~~json
{
  "source": "00aeafa4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeafac`](#insn-00aeafac)

~~~json
{
  "source": "00aeafac",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeafb4`](#insn-00aeafb4)

~~~json
{
  "source": "00aeafb4",
  "target": "00aeb02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeafbc`](#insn-00aeafbc)

~~~json
{
  "source": "00aeafbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeafc0`](#insn-00aeafc0)

~~~json
{
  "source": "00aeafc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeafc4`](#insn-00aeafc4)

~~~json
{
  "source": "00aeafc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeafc8`](#insn-00aeafc8)

~~~json
{
  "source": "00aeafc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeafcc`](#insn-00aeafcc)

~~~json
{
  "source": "00aeafcc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeafd0`](#insn-00aeafd0)

~~~json
{
  "source": "00aeafd0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeafdc`](#insn-00aeafdc)

~~~json
{
  "source": "00aeafdc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeafe4`](#insn-00aeafe4)

~~~json
{
  "source": "00aeafe4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeafec`](#insn-00aeafec)

~~~json
{
  "source": "00aeafec",
  "target": "00aeb02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaff4`](#insn-00aeaff4)

~~~json
{
  "source": "00aeaff4",
  "target": "00470880",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeb02c`](#insn-00aeb02c)

~~~json
{
  "source": "00aeb02c",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
