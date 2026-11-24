# 00bbaca8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbac0c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbac0c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0079.md#compare-47e4c92410456f3281f1774ac33e3499)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bbbc9c`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbc9c.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0079.md#compare-d4a88090898fa3a5d7b0243324a3ea70)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaca8",
  "name": "FUN_00bbaca8",
  "size": 372,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5203374b575deea6569ec5f8af4b4868c140f578c85489b5ca078e7d986c21a6",
  "source_text_sha256": "5203374b575deea6569ec5f8af4b4868c140f578c85489b5ca078e7d986c21a6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbaca8",
        "00bbae1b"
      ]
    ],
    "bytes_sha256": "bfab24ccb9868c7dcf3119e6ba7abc7cdf8bfb7ad1eb169a940e6c83be4ec688",
    "instruction_count": 93,
    "instruction_bytes": 372,
    "body_bytes": 372,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57fb0](../00c57/00c57fb0.md)
- [00c58190](../00c58/00c58190.md)
- [00c5aad0](../00c5a/00c5aad0.md)
- [00c5aae0](../00c5a/00c5aae0.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5b200](../00c5b/00c5b200.md)
- [00c5bfd0](../00c5b/00c5bfd0.md)
- [00c5d670](../00c5d/00c5d670.md)
- [00c5d6c0](../00c5d/00c5d6c0.md)
- [00c5d6d0](../00c5d/00c5d6d0.md)
- [00c5d720](../00c5d/00c5d720.md)

## 関連文字列（未確認候補）

~~~text
"Reading message file, errno=%d"
"file_descriptor >= 0"
"watch_descriptor >= 0"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1859 bytes

~~~c

undefined8 FUN_00bbaca8(void)

{
  long lVar1;
  int __fd;
  int iVar2;
  long lVar3;
  ssize_t sVar4;
  undefined4 *puVar5;
  char *pcVar6;
  byte *__name;
  undefined1 auStack_180 [12];
  int local_174 [65];
  long local_70;
  
  lVar1 = tpidr_el0;
  local_70 = *(long *)(lVar1 + 0x28);
  _ZN8firebase5Mutex7AcquireEv(&DAT_01126358);
  if (DAT_01126460 == 0) {
    lVar3 = 0;
  }
  else {
    lVar3 = _ZNK8firebase3App7java_vmEv();
  }
  _ZN8firebase5Mutex7ReleaseEv(&DAT_01126358);
  if (lVar3 != 0) {
    __fd = inotify_init();
    if (__fd < 0) {
      pcVar6 = "file_descriptor >= 0";
    }
    else {
      if ((*DAT_01126468 & 1) == 0) {
        __name = DAT_01126468 + 1;
      }
      else {
        __name = *(byte **)(DAT_01126468 + 0x10);
      }
      iVar2 = inotify_add_watch(__fd,(char *)__name,8);
      if (-1 < iVar2) {
        do {
          _ZN8firebase9messaging15ProcessMessagesEv();
          while( true ) {
            sVar4 = read(__fd,auStack_180,0x110);
            _ZN8firebase5Mutex7AcquireEv(&DAT_01126358);
            lVar3 = DAT_01126460;
            _ZN8firebase5Mutex7ReleaseEv(&DAT_01126358);
            if (lVar3 == 0) goto LAB_00bbade4;
            if (sVar4 < 1) break;
            lVar3 = 0;
            do {
              _ZN8firebase9messaging15ProcessMessagesEv();
              lVar3 = (long)((int)lVar3 + *(int *)((long)local_174 + lVar3) + 0x10);
            } while (lVar3 < sVar4);
          }
          puVar5 = (undefined4 *)__errno();
          _ZN8firebase8LogDebugEPKcz("Reading message file, errno=%d",*puVar5);
        } while( true );
      }
      pcVar6 = "watch_descriptor >= 0";
    }
    _ZN8firebase9LogAssertEPKcz(pcVar6);
  }
LAB_00bbade4:
  if (*(long *)(lVar1 + 0x28) != local_70) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbaca8"></a> `00bbaca8` | `ff 03 06 d1` | sub sp,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbacac"></a> `00bbacac` | `fc 6f 12 a9` | stp x28,x27,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00bbacb0"></a> `00bbacb0` | `fa 67 13 a9` | stp x26,x25,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00bbacb4"></a> `00bbacb4` | `f8 5f 14 a9` | stp x24,x23,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00bbacb8"></a> `00bbacb8` | `f6 57 15 a9` | stp x22,x21,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00bbacbc"></a> `00bbacbc` | `f4 4f 16 a9` | stp x20,x19,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-00bbacc0"></a> `00bbacc0` | `fd 7b 17 a9` | stp x29,x30,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00bbacc4"></a> `00bbacc4` | `fd c3 05 91` | add x29,sp,#0x170 | `FALL_THROUGH`
<a id="insn-00bbacc8"></a> `00bbacc8` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bbaccc"></a> `00bbaccc` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00bbacd0"></a> `00bbacd0` | `60 2b 00 90` | adrp x0,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbacd4"></a> `00bbacd4` | `00 60 0d 91` | add x0,x0,#0x358 | `FALL_THROUGH`
<a id="insn-00bbacd8"></a> `00bbacd8` | `a8 03 1a f8` | stur x8,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00bbacdc"></a> `00bbacdc` | `7d 7f 02 94` | bl 0x00c5aad0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbace0"></a> `00bbace0` | `78 2b 00 90` | adrp x24,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbace4"></a> `00bbace4` | `00 33 42 f9` | ldr x0,[x24, #0x460] | `FALL_THROUGH`
<a id="insn-00bbace8"></a> `00bbace8` | `80 00 00 b4` | cbz x0,0x00bbacf8 | `CONDITIONAL_JUMP`
<a id="insn-00bbacec"></a> `00bbacec` | `b9 84 02 94` | bl 0x00c5bfd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbacf0"></a> `00bbacf0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbacf4"></a> `00bbacf4` | `02 00 00 14` | b 0x00bbacfc | `UNCONDITIONAL_JUMP`
<a id="insn-00bbacf8"></a> `00bbacf8` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-00bbacfc"></a> `00bbacfc` | `60 2b 00 90` | adrp x0,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbad00"></a> `00bbad00` | `00 60 0d 91` | add x0,x0,#0x358 | `FALL_THROUGH`
<a id="insn-00bbad04"></a> `00bbad04` | `77 7f 02 94` | bl 0x00c5aae0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbad08"></a> `00bbad08` | `f3 06 00 b4` | cbz x19,0x00bbade4 | `CONDITIONAL_JUMP`
<a id="insn-00bbad0c"></a> `00bbad0c` | `71 8a 02 94` | bl 0x00c5d6d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbad10"></a> `00bbad10` | `00 01 f8 37` | tbnz w0,#0x1f,0x00bbad30 | `CONDITIONAL_JUMP`
<a id="insn-00bbad14"></a> `00bbad14` | `68 2b 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbad18"></a> `00bbad18` | `08 35 42 f9` | ldr x8,[x8, #0x468] | `FALL_THROUGH`
<a id="insn-00bbad1c"></a> `00bbad1c` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bbad20"></a> `00bbad20` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbad24"></a> `00bbad24` | `c9 00 00 37` | tbnz w9,#0x0,0x00bbad3c | `CONDITIONAL_JUMP`
<a id="insn-00bbad28"></a> `00bbad28` | `01 05 00 91` | add x1,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbad2c"></a> `00bbad2c` | `05 00 00 14` | b 0x00bbad40 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbad30"></a> `00bbad30` | `a0 b7 ff 90` | adrp x0,0x2ae000 | `FALL_THROUGH`
<a id="insn-00bbad34"></a> `00bbad34` | `00 80 0d 91` | add x0,x0,#0x360 | `FALL_THROUGH`
<a id="insn-00bbad38"></a> `00bbad38` | `2a 00 00 14` | b 0x00bbade0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbad3c"></a> `00bbad3c` | `01 09 40 f9` | ldr x1,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bbad40"></a> `00bbad40` | `02 01 80 52` | mov w2,#0x8 | `FALL_THROUGH`
<a id="insn-00bbad44"></a> `00bbad44` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00bbad48"></a> `00bbad48` | `5e 8a 02 94` | bl 0x00c5d6c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbad4c"></a> `00bbad4c` | `60 04 f8 37` | tbnz w0,#0x1f,0x00bbadd8 | `CONDITIONAL_JUMP`
<a id="insn-00bbad50"></a> `00bbad50` | `74 2b 00 90` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbad54"></a> `00bbad54` | `75 b7 ff f0` | adrp x21,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bbad58"></a> `00bbad58` | `f9 03 00 91` | mov x25,sp | `FALL_THROUGH`
<a id="insn-00bbad5c"></a> `00bbad5c` | `94 62 0d 91` | add x20,x20,#0x358 | `FALL_THROUGH`
<a id="insn-00bbad60"></a> `00bbad60` | `b5 96 20 91` | add x21,x21,#0x825 | `FALL_THROUGH`
<a id="insn-00bbad64"></a> `00bbad64` | `43 8a 02 94` | bl 0x00c5d670 | `UNCONDITIONAL_CALL`
<a id="insn-00bbad68"></a> `00bbad68` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bbad6c"></a> `00bbad6c` | `02 22 80 52` | mov w2,#0x110 | `FALL_THROUGH`
<a id="insn-00bbad70"></a> `00bbad70` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00bbad74"></a> `00bbad74` | `6b 8a 02 94` | bl 0x00c5d720 | `UNCONDITIONAL_CALL`
<a id="insn-00bbad78"></a> `00bbad78` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbad7c"></a> `00bbad7c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbad80"></a> `00bbad80` | `54 7f 02 94` | bl 0x00c5aad0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbad84"></a> `00bbad84` | `1a 33 42 f9` | ldr x26,[x24, #0x460] | `FALL_THROUGH`
<a id="insn-00bbad88"></a> `00bbad88` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbad8c"></a> `00bbad8c` | `55 7f 02 94` | bl 0x00c5aae0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbad90"></a> `00bbad90` | `ba 02 00 b4` | cbz x26,0x00bbade4 | `CONDITIONAL_JUMP`
<a id="insn-00bbad94"></a> `00bbad94` | `df 06 00 f1` | cmp x22,#0x1 | `FALL_THROUGH`
<a id="insn-00bbad98"></a> `00bbad98` | `6b 01 00 54` | b.lt 0x00bbadc4 | `CONDITIONAL_JUMP`
<a id="insn-00bbad9c"></a> `00bbad9c` | `fa 03 1f aa` | mov x26,xzr | `FALL_THROUGH`
<a id="insn-00bbada0"></a> `00bbada0` | `3b 03 1a 8b` | add x27,x25,x26 | `FALL_THROUGH`
<a id="insn-00bbada4"></a> `00bbada4` | `33 8a 02 94` | bl 0x00c5d670 | `UNCONDITIONAL_CALL`
<a id="insn-00bbada8"></a> `00bbada8` | `68 0f 40 b9` | ldr w8,[x27, #0xc] | `FALL_THROUGH`
<a id="insn-00bbadac"></a> `00bbadac` | `48 03 08 0b` | add w8,w26,w8 | `FALL_THROUGH`
<a id="insn-00bbadb0"></a> `00bbadb0` | `08 41 00 11` | add w8,w8,#0x10 | `FALL_THROUGH`
<a id="insn-00bbadb4"></a> `00bbadb4` | `1a 7d 40 93` | sxtw x26,w8 | `FALL_THROUGH`
<a id="insn-00bbadb8"></a> `00bbadb8` | `5f 03 16 eb` | cmp x26,x22 | `FALL_THROUGH`
<a id="insn-00bbadbc"></a> `00bbadbc` | `2b ff ff 54` | b.lt 0x00bbada0 | `CONDITIONAL_JUMP`
<a id="insn-00bbadc0"></a> `00bbadc0` | `ea ff ff 17` | b 0x00bbad68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbadc4"></a> `00bbadc4` | `f3 74 02 94` | bl 0x00c58190 | `UNCONDITIONAL_CALL`
<a id="insn-00bbadc8"></a> `00bbadc8` | `01 00 40 b9` | ldr w1,[x0] | `FALL_THROUGH`
<a id="insn-00bbadcc"></a> `00bbadcc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbadd0"></a> `00bbadd0` | `0c 81 02 94` | bl 0x00c5b200 | `UNCONDITIONAL_CALL`
<a id="insn-00bbadd4"></a> `00bbadd4` | `e4 ff ff 17` | b 0x00bbad64 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbadd8"></a> `00bbadd8` | `20 b8 ff b0` | adrp x0,0x2bf000 | `FALL_THROUGH`
<a id="insn-00bbaddc"></a> `00bbaddc` | `00 8c 26 91` | add x0,x0,#0x9a3 | `FALL_THROUGH`
<a id="insn-00bbade0"></a> `00bbade0` | `bc 80 02 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbade4"></a> `00bbade4` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00bbade8"></a> `00bbade8` | `a9 03 5a f8` | ldur x9,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00bbadec"></a> `00bbadec` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbadf0"></a> `00bbadf0` | `41 01 00 54` | b.ne 0x00bbae18 | `CONDITIONAL_JUMP`
<a id="insn-00bbadf4"></a> `00bbadf4` | `fd 7b 57 a9` | ldp x29,x30,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00bbadf8"></a> `00bbadf8` | `f4 4f 56 a9` | ldp x20,x19,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-00bbadfc"></a> `00bbadfc` | `f6 57 55 a9` | ldp x22,x21,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00bbae00"></a> `00bbae00` | `f8 5f 54 a9` | ldp x24,x23,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00bbae04"></a> `00bbae04` | `fa 67 53 a9` | ldp x26,x25,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00bbae08"></a> `00bbae08` | `fc 6f 52 a9` | ldp x28,x27,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00bbae0c"></a> `00bbae0c` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bbae10"></a> `00bbae10` | `ff 03 06 91` | add sp,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbae14"></a> `00bbae14` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbae18"></a> `00bbae18` | `66 74 02 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbaca8`](#insn-00bbaca8) 範囲 `[['00bbaca8', '00bbaceb']]`
  - `CONDITIONAL_JUMP` [`00bbace8`](#insn-00bbace8) → [`00bbacf8`](#insn-00bbacf8)
  - `FALL_THROUGH` [`00bbace8`](#insn-00bbace8) → [`00bbacec`](#insn-00bbacec)
- ブロック [`00bbacec`](#insn-00bbacec) 範囲 `[['00bbacec', '00bbacf7']]`
  - `UNCONDITIONAL_JUMP` [`00bbacf4`](#insn-00bbacf4) → [`00bbacfc`](#insn-00bbacfc)
- ブロック [`00bbacf8`](#insn-00bbacf8) 範囲 `[['00bbacf8', '00bbacfb']]`
  - `FALL_THROUGH` [`00bbacf8`](#insn-00bbacf8) → [`00bbacfc`](#insn-00bbacfc)
- ブロック [`00bbacfc`](#insn-00bbacfc) 範囲 `[['00bbacfc', '00bbad0b']]`
  - `CONDITIONAL_JUMP` [`00bbad08`](#insn-00bbad08) → [`00bbade4`](#insn-00bbade4)
  - `FALL_THROUGH` [`00bbad08`](#insn-00bbad08) → [`00bbad0c`](#insn-00bbad0c)
- ブロック [`00bbad0c`](#insn-00bbad0c) 範囲 `[['00bbad0c', '00bbad13']]`
  - `CONDITIONAL_JUMP` [`00bbad10`](#insn-00bbad10) → [`00bbad30`](#insn-00bbad30)
  - `FALL_THROUGH` [`00bbad10`](#insn-00bbad10) → [`00bbad14`](#insn-00bbad14)
- ブロック [`00bbad14`](#insn-00bbad14) 範囲 `[['00bbad14', '00bbad27']]`
  - `CONDITIONAL_JUMP` [`00bbad24`](#insn-00bbad24) → [`00bbad3c`](#insn-00bbad3c)
  - `FALL_THROUGH` [`00bbad24`](#insn-00bbad24) → [`00bbad28`](#insn-00bbad28)
- ブロック [`00bbad28`](#insn-00bbad28) 範囲 `[['00bbad28', '00bbad2f']]`
  - `UNCONDITIONAL_JUMP` [`00bbad2c`](#insn-00bbad2c) → [`00bbad40`](#insn-00bbad40)
- ブロック [`00bbad30`](#insn-00bbad30) 範囲 `[['00bbad30', '00bbad3b']]`
  - `UNCONDITIONAL_JUMP` [`00bbad38`](#insn-00bbad38) → [`00bbade0`](#insn-00bbade0)
- ブロック [`00bbad3c`](#insn-00bbad3c) 範囲 `[['00bbad3c', '00bbad3f']]`
  - `FALL_THROUGH` [`00bbad3c`](#insn-00bbad3c) → [`00bbad40`](#insn-00bbad40)
- ブロック [`00bbad40`](#insn-00bbad40) 範囲 `[['00bbad40', '00bbad4f']]`
  - `CONDITIONAL_JUMP` [`00bbad4c`](#insn-00bbad4c) → [`00bbadd8`](#insn-00bbadd8)
  - `FALL_THROUGH` [`00bbad4c`](#insn-00bbad4c) → [`00bbad50`](#insn-00bbad50)
- ブロック [`00bbad50`](#insn-00bbad50) 範囲 `[['00bbad50', '00bbad63']]`
  - `FALL_THROUGH` [`00bbad60`](#insn-00bbad60) → [`00bbad64`](#insn-00bbad64)
- ブロック [`00bbad64`](#insn-00bbad64) 範囲 `[['00bbad64', '00bbad67']]`
  - `FALL_THROUGH` [`00bbad64`](#insn-00bbad64) → [`00bbad68`](#insn-00bbad68)
- ブロック [`00bbad68`](#insn-00bbad68) 範囲 `[['00bbad68', '00bbad93']]`
  - `CONDITIONAL_JUMP` [`00bbad90`](#insn-00bbad90) → [`00bbade4`](#insn-00bbade4)
  - `FALL_THROUGH` [`00bbad90`](#insn-00bbad90) → [`00bbad94`](#insn-00bbad94)
- ブロック [`00bbad94`](#insn-00bbad94) 範囲 `[['00bbad94', '00bbad9b']]`
  - `CONDITIONAL_JUMP` [`00bbad98`](#insn-00bbad98) → [`00bbadc4`](#insn-00bbadc4)
  - `FALL_THROUGH` [`00bbad98`](#insn-00bbad98) → [`00bbad9c`](#insn-00bbad9c)
- ブロック [`00bbad9c`](#insn-00bbad9c) 範囲 `[['00bbad9c', '00bbad9f']]`
  - `FALL_THROUGH` [`00bbad9c`](#insn-00bbad9c) → [`00bbada0`](#insn-00bbada0)
- ブロック [`00bbada0`](#insn-00bbada0) 範囲 `[['00bbada0', '00bbadbf']]`
  - `CONDITIONAL_JUMP` [`00bbadbc`](#insn-00bbadbc) → [`00bbada0`](#insn-00bbada0)
  - `FALL_THROUGH` [`00bbadbc`](#insn-00bbadbc) → [`00bbadc0`](#insn-00bbadc0)
- ブロック [`00bbadc0`](#insn-00bbadc0) 範囲 `[['00bbadc0', '00bbadc3']]`
  - `UNCONDITIONAL_JUMP` [`00bbadc0`](#insn-00bbadc0) → [`00bbad68`](#insn-00bbad68)
- ブロック [`00bbadc4`](#insn-00bbadc4) 範囲 `[['00bbadc4', '00bbadd7']]`
  - `UNCONDITIONAL_JUMP` [`00bbadd4`](#insn-00bbadd4) → [`00bbad64`](#insn-00bbad64)
- ブロック [`00bbadd8`](#insn-00bbadd8) 範囲 `[['00bbadd8', '00bbaddf']]`
  - `FALL_THROUGH` [`00bbaddc`](#insn-00bbaddc) → [`00bbade0`](#insn-00bbade0)
- ブロック [`00bbade0`](#insn-00bbade0) 範囲 `[['00bbade0', '00bbade3']]`
  - `FALL_THROUGH` [`00bbade0`](#insn-00bbade0) → [`00bbade4`](#insn-00bbade4)
- ブロック [`00bbade4`](#insn-00bbade4) 範囲 `[['00bbade4', '00bbadf3']]`
  - `CONDITIONAL_JUMP` [`00bbadf0`](#insn-00bbadf0) → [`00bbae18`](#insn-00bbae18)
  - `FALL_THROUGH` [`00bbadf0`](#insn-00bbadf0) → [`00bbadf4`](#insn-00bbadf4)
- ブロック [`00bbadf4`](#insn-00bbadf4) 範囲 `[['00bbadf4', '00bbae17']]`
- ブロック [`00bbae18`](#insn-00bbae18) 範囲 `[['00bbae18', '00bbae1b']]`

## 命令位置別の参照

- [`00bbacac`](#insn-00bbacac) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacb0`](#insn-00bbacb0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacb4`](#insn-00bbacb4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacb8`](#insn-00bbacb8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacbc`](#insn-00bbacbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacc0`](#insn-00bbacc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacd4`](#insn-00bbacd4) → `01126358`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacd8`](#insn-00bbacd8) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacdc`](#insn-00bbacdc) → [`00c5aad0`](../00c5a/00c5aad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aad0` · 推定シンボル `None` · 推定型 `None`
- [`00bbace4`](#insn-00bbace4) → `01126460`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbace8`](#insn-00bbace8) → [`00bbacf8`](#insn-00bbacf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacec`](#insn-00bbacec) → [`00c5bfd0`](../00c5b/00c5bfd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfd0` · 推定シンボル `None` · 推定型 `None`
- [`00bbacf4`](#insn-00bbacf4) → [`00bbacfc`](#insn-00bbacfc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad00`](#insn-00bbad00) → `01126358`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad04`](#insn-00bbad04) → [`00c5aae0`](../00c5a/00c5aae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aae0` · 推定シンボル `None` · 推定型 `None`
- [`00bbad08`](#insn-00bbad08) → [`00bbade4`](#insn-00bbade4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad0c`](#insn-00bbad0c) → [`00c5d6d0`](../00c5d/00c5d6d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d6d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbad10`](#insn-00bbad10) → [`00bbad30`](#insn-00bbad30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad18`](#insn-00bbad18) → `01126468`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbad24`](#insn-00bbad24) → [`00bbad3c`](#insn-00bbad3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad2c`](#insn-00bbad2c) → [`00bbad40`](#insn-00bbad40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad34`](#insn-00bbad34) → `002ae360`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbad38`](#insn-00bbad38) → [`00bbade0`](#insn-00bbade0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad48`](#insn-00bbad48) → [`00c5d6c0`](../00c5d/00c5d6c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d6c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbad4c`](#insn-00bbad4c) → [`00bbadd8`](#insn-00bbadd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad64`](#insn-00bbad64) → [`00c5d670`](../00c5d/00c5d670.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d670` · 推定シンボル `None` · 推定型 `None`
- [`00bbad74`](#insn-00bbad74) → [`00c5d720`](../00c5d/00c5d720.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d720` · 推定シンボル `None` · 推定型 `None`
- [`00bbad7c`](#insn-00bbad7c) → `01126358`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad80`](#insn-00bbad80) → [`00c5aad0`](../00c5a/00c5aad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aad0` · 推定シンボル `None` · 推定型 `None`
- [`00bbad84`](#insn-00bbad84) → `01126460`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbad88`](#insn-00bbad88) → `01126358`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad8c`](#insn-00bbad8c) → [`00c5aae0`](../00c5a/00c5aae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aae0` · 推定シンボル `None` · 推定型 `None`
- [`00bbad90`](#insn-00bbad90) → [`00bbade4`](#insn-00bbade4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad98`](#insn-00bbad98) → [`00bbadc4`](#insn-00bbadc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbada4`](#insn-00bbada4) → [`00c5d670`](../00c5d/00c5d670.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d670` · 推定シンボル `None` · 推定型 `None`
- [`00bbada8`](#insn-00bbada8) → `Stack[-0x174]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadbc`](#insn-00bbadbc) → [`00bbada0`](#insn-00bbada0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadc0`](#insn-00bbadc0) → [`00bbad68`](#insn-00bbad68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadc4`](#insn-00bbadc4) → [`00c58190`](../00c58/00c58190.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58190` · 推定シンボル `None` · 推定型 `None`
- [`00bbadcc`](#insn-00bbadcc) → `002a9825`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbadd0`](#insn-00bbadd0) → [`00c5b200`](../00c5b/00c5b200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b200` · 推定シンボル `None` · 推定型 `None`
- [`00bbadd4`](#insn-00bbadd4) → [`00bbad64`](#insn-00bbad64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaddc`](#insn-00bbaddc) → `002bf9a3`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbade0`](#insn-00bbade0) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbade8`](#insn-00bbade8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadf0`](#insn-00bbadf0) → [`00bbae18`](#insn-00bbae18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadf4`](#insn-00bbadf4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadf8`](#insn-00bbadf8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadfc`](#insn-00bbadfc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae00`](#insn-00bbae00) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae04`](#insn-00bbae04) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae08`](#insn-00bbae08) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae18`](#insn-00bbae18) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbacac`](#insn-00bbacac)

~~~json
{
  "source": "00bbacac",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacb0`](#insn-00bbacb0)

~~~json
{
  "source": "00bbacb0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacb4`](#insn-00bbacb4)

~~~json
{
  "source": "00bbacb4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacb8`](#insn-00bbacb8)

~~~json
{
  "source": "00bbacb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacbc`](#insn-00bbacbc)

~~~json
{
  "source": "00bbacbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacc0`](#insn-00bbacc0)

~~~json
{
  "source": "00bbacc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacd4`](#insn-00bbacd4)

~~~json
{
  "source": "00bbacd4",
  "target": "01126358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacd8`](#insn-00bbacd8)

~~~json
{
  "source": "00bbacd8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacdc`](#insn-00bbacdc)

~~~json
{
  "source": "00bbacdc",
  "target": "00c5aad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbace4`](#insn-00bbace4)

~~~json
{
  "source": "00bbace4",
  "target": "01126460",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126460",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbace8`](#insn-00bbace8)

~~~json
{
  "source": "00bbace8",
  "target": "00bbacf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacec`](#insn-00bbacec)

~~~json
{
  "source": "00bbacec",
  "target": "00c5bfd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbacf4`](#insn-00bbacf4)

~~~json
{
  "source": "00bbacf4",
  "target": "00bbacfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad00`](#insn-00bbad00)

~~~json
{
  "source": "00bbad00",
  "target": "01126358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad04`](#insn-00bbad04)

~~~json
{
  "source": "00bbad04",
  "target": "00c5aae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbad08`](#insn-00bbad08)

~~~json
{
  "source": "00bbad08",
  "target": "00bbade4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad0c`](#insn-00bbad0c)

~~~json
{
  "source": "00bbad0c",
  "target": "00c5d6d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbad10`](#insn-00bbad10)

~~~json
{
  "source": "00bbad10",
  "target": "00bbad30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad18`](#insn-00bbad18)

~~~json
{
  "source": "00bbad18",
  "target": "01126468",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126468",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbad24`](#insn-00bbad24)

~~~json
{
  "source": "00bbad24",
  "target": "00bbad3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad2c`](#insn-00bbad2c)

~~~json
{
  "source": "00bbad2c",
  "target": "00bbad40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad34`](#insn-00bbad34)

~~~json
{
  "source": "00bbad34",
  "target": "002ae360",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ae360",
  "offset": 0,
  "size": 21,
  "datatype": "string",
  "bytes": "66696c655f64657363726970746f72203e3d203000",
  "capture_start": "002ae360",
  "capture_bytes": 21,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbad38`](#insn-00bbad38)

~~~json
{
  "source": "00bbad38",
  "target": "00bbade0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad48`](#insn-00bbad48)

~~~json
{
  "source": "00bbad48",
  "target": "00c5d6c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbad4c`](#insn-00bbad4c)

~~~json
{
  "source": "00bbad4c",
  "target": "00bbadd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad64`](#insn-00bbad64)

~~~json
{
  "source": "00bbad64",
  "target": "00c5d670",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbad74`](#insn-00bbad74)

~~~json
{
  "source": "00bbad74",
  "target": "00c5d720",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbad7c`](#insn-00bbad7c)

~~~json
{
  "source": "00bbad7c",
  "target": "01126358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad80`](#insn-00bbad80)

~~~json
{
  "source": "00bbad80",
  "target": "00c5aad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbad84`](#insn-00bbad84)

~~~json
{
  "source": "00bbad84",
  "target": "01126460",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126460",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbad88`](#insn-00bbad88)

~~~json
{
  "source": "00bbad88",
  "target": "01126358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad8c`](#insn-00bbad8c)

~~~json
{
  "source": "00bbad8c",
  "target": "00c5aae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbad90`](#insn-00bbad90)

~~~json
{
  "source": "00bbad90",
  "target": "00bbade4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad98`](#insn-00bbad98)

~~~json
{
  "source": "00bbad98",
  "target": "00bbadc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbada4`](#insn-00bbada4)

~~~json
{
  "source": "00bbada4",
  "target": "00c5d670",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbada8`](#insn-00bbada8)

~~~json
{
  "source": "00bbada8",
  "target": "Stack[-0x174]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadbc`](#insn-00bbadbc)

~~~json
{
  "source": "00bbadbc",
  "target": "00bbada0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadc0`](#insn-00bbadc0)

~~~json
{
  "source": "00bbadc0",
  "target": "00bbad68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadc4`](#insn-00bbadc4)

~~~json
{
  "source": "00bbadc4",
  "target": "00c58190",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbadcc`](#insn-00bbadcc)

~~~json
{
  "source": "00bbadcc",
  "target": "002a9825",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a9825",
  "offset": 0,
  "size": 31,
  "datatype": "string",
  "bytes": "52656164696e67206d6573736167652066696c652c206572726e6f3d256400",
  "capture_start": "002a9825",
  "capture_bytes": 31,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbadd0`](#insn-00bbadd0)

~~~json
{
  "source": "00bbadd0",
  "target": "00c5b200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbadd4`](#insn-00bbadd4)

~~~json
{
  "source": "00bbadd4",
  "target": "00bbad64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaddc`](#insn-00bbaddc)

~~~json
{
  "source": "00bbaddc",
  "target": "002bf9a3",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bf9a3",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "77617463685f64657363726970746f72203e3d203000",
  "capture_start": "002bf9a3",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbade0`](#insn-00bbade0)

~~~json
{
  "source": "00bbade0",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbade8`](#insn-00bbade8)

~~~json
{
  "source": "00bbade8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadf0`](#insn-00bbadf0)

~~~json
{
  "source": "00bbadf0",
  "target": "00bbae18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadf4`](#insn-00bbadf4)

~~~json
{
  "source": "00bbadf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadf8`](#insn-00bbadf8)

~~~json
{
  "source": "00bbadf8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadfc`](#insn-00bbadfc)

~~~json
{
  "source": "00bbadfc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae00`](#insn-00bbae00)

~~~json
{
  "source": "00bbae00",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae04`](#insn-00bbae04)

~~~json
{
  "source": "00bbae04",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae08`](#insn-00bbae08)

~~~json
{
  "source": "00bbae08",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae18`](#insn-00bbae18)

~~~json
{
  "source": "00bbae18",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
