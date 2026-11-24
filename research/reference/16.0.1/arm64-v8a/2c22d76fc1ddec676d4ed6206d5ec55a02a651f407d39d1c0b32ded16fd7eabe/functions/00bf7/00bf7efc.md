# 00bf7efc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bf7ad4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7ad4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-600ca7d93a4b8429f2b585815e593854)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bf7f98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf7/00bf7f98.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0086.md#compare-e9c4c913c65ec5f400fcdb047ee00e5c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf7efc",
  "name": "_ZNSt6__ndk110to_wstringEd",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "26a6b77bc594483e50a1e6b21a348ce906e0f4db86011a7fb5217fce56703bb6",
  "source_text_sha256": "26a6b77bc594483e50a1e6b21a348ce906e0f4db86011a7fb5217fce56703bb6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf7efc",
        "00bf8023"
      ]
    ],
    "bytes_sha256": "7be08178b7efeda6e9ef8ab8f6bef0a1c0bac78130413d1f7ac415e2039df9ef",
    "instruction_count": 74,
    "instruction_bytes": 296,
    "body_bytes": 296,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57e90](../00c57/00c57e90.md)
- [00c5a890](../00c5a/00c5a890.md)
- [00c5e110](../00c5e/00c5e110.md)
- [00c5e120](../00c5e/00c5e120.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1998 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void _ZNSt6__ndk110to_wstringEd(ulong *param_1,undefined8 param_2)

{
  wchar_t *pwVar1;
  uint uVar2;
  ulong uVar3;
  ulong uVar4;
  ulong local_60;
  ulong uStack_58;
  wchar_t *local_50;
  
  local_50 = (wchar_t *)_Znwm(0x58);
  uStack_58 = _UNK_002c3288;
  local_60 = _DAT_002c3280;
  local_50[0x14] = L'\0';
  local_50[2] = L'\0';
  local_50[3] = L'\0';
  local_50[0] = L'\0';
  local_50[1] = L'\0';
  local_50[6] = L'\0';
  local_50[7] = L'\0';
  local_50[4] = L'\0';
  local_50[5] = L'\0';
  local_50[10] = L'\0';
  local_50[0xb] = L'\0';
  local_50[8] = L'\0';
  local_50[9] = L'\0';
  local_50[0xe] = L'\0';
  local_50[0xf] = L'\0';
  local_50[0xc] = L'\0';
  local_50[0xd] = L'\0';
  local_50[0x12] = L'\0';
  local_50[0x13] = L'\0';
  local_50[0x10] = L'\0';
  local_50[0x11] = L'\0';
  _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6resizeEmw(&local_60,0x15,0);
  uVar4 = (ulong)((byte)local_60 >> 1);
  if ((local_60 & 1) != 0) {
    uVar4 = uStack_58;
  }
  do {
    pwVar1 = (wchar_t *)((ulong)&local_60 | 4);
    if (((byte)local_60 & 1) != 0) {
      pwVar1 = local_50;
    }
    uVar2 = swprintf(pwVar1,uVar4 + 1,L"%f",param_2);
    if ((int)uVar2 < 0) {
      uVar3 = uVar4 << 1 | 1;
    }
    else {
      uVar3 = (ulong)uVar2;
      if (uVar3 <= uVar4) {
        _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6resizeEmw
                  (&local_60,uVar3,0);
        pwVar1 = local_50;
        uVar4 = uStack_58;
        uStack_58 = 0;
        local_50 = (wchar_t *)0x0;
        param_1[1] = uVar4;
        *param_1 = local_60;
        param_1[2] = (ulong)pwVar1;
        local_60 = 0;
        _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEED1Ev(&local_60);
        return;
      }
    }
    _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6resizeEmw(&local_60,uVar3,0);
    uVar4 = uVar3;
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf7efc"></a> `00bf7efc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf7f00"></a> `00bf7f00` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bf7f04"></a> `00bf7f04` | `e8 13 00 fd` | str d8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf7f08"></a> `00bf7f08` | `fd fb 02 a9` | stp x29,x30,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bf7f0c"></a> `00bf7f0c` | `f7 1f 00 f9` | str x23,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bf7f10"></a> `00bf7f10` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bf7f14"></a> `00bf7f14` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bf7f18"></a> `00bf7f18` | `fd a3 00 91` | add x29,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00bf7f1c"></a> `00bf7f1c` | `00 0b 80 52` | mov w0,#0x58 | `FALL_THROUGH`
<a id="insn-00bf7f20"></a> `00bf7f20` | `08 40 60 1e` | fmov d8,d0 | `FALL_THROUGH`
<a id="insn-00bf7f24"></a> `00bf7f24` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bf7f28"></a> `00bf7f28` | `da 7f 01 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bf7f2c"></a> `00bf7f2c` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bf7f30"></a> `00bf7f30` | `68 b6 ff 90` | adrp x8,0x2c3000 | `FALL_THROUGH`
<a id="insn-00bf7f34"></a> `00bf7f34` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf7f38"></a> `00bf7f38` | `01 a1 c0 3d` | ldr q1,[x8, #0x280] | `FALL_THROUGH`
<a id="insn-00bf7f3c"></a> `00bf7f3c` | `1f 50 00 b9` | str wzr,[x0, #0x50] | `FALL_THROUGH`
<a id="insn-00bf7f40"></a> `00bf7f40` | `e1 03 80 3d` | str q1,[sp] | `FALL_THROUGH`
<a id="insn-00bf7f44"></a> `00bf7f44` | `00 00 00 ad` | stp q0,q0,[x0] | `FALL_THROUGH`
<a id="insn-00bf7f48"></a> `00bf7f48` | `00 00 01 ad` | stp q0,q0,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bf7f4c"></a> `00bf7f4c` | `00 10 80 3d` | str q0,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00bf7f50"></a> `00bf7f50` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bf7f54"></a> `00bf7f54` | `a1 02 80 52` | mov w1,#0x15 | `FALL_THROUGH`
<a id="insn-00bf7f58"></a> `00bf7f58` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00bf7f5c"></a> `00bf7f5c` | `f4 03 00 91` | mov x20,sp | `FALL_THROUGH`
<a id="insn-00bf7f60"></a> `00bf7f60` | `4c 8a 01 94` | bl 0x00c5a890 | `UNCONDITIONAL_CALL`
<a id="insn-00bf7f64"></a> `00bf7f64` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00bf7f68"></a> `00bf7f68` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bf7f6c"></a> `00bf7f6c` | `96 02 7e b2` | orr x22,x20,#0x4 | `FALL_THROUGH`
<a id="insn-00bf7f70"></a> `00bf7f70` | `d4 b8 ff b0` | adrp x20,0x310000 | `FALL_THROUGH`
<a id="insn-00bf7f74"></a> `00bf7f74` | `94 d2 13 91` | add x20,x20,#0x4f4 | `FALL_THROUGH`
<a id="insn-00bf7f78"></a> `00bf7f78` | `37 00 80 52` | mov w23,#0x1 | `FALL_THROUGH`
<a id="insn-00bf7f7c"></a> `00bf7f7c` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf7f80"></a> `00bf7f80` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf7f84"></a> `00bf7f84` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bf7f88"></a> `00bf7f88` | `e9 0b 40 f9` | ldr x9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf7f8c"></a> `00bf7f8c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf7f90"></a> `00bf7f90` | `c0 02 89 9a` | csel x0,x22,x9,eq | `FALL_THROUGH`
<a id="insn-00bf7f94"></a> `00bf7f94` | `00 41 60 1e` | fmov d0,d8 | `FALL_THROUGH`
<a id="insn-00bf7f98"></a> `00bf7f98` | `a1 06 00 91` | add x1,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bf7f9c"></a> `00bf7f9c` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00bf7fa0"></a> `00bf7fa0` | `5c 98 01 94` | bl 0x00c5e110 | `UNCONDITIONAL_CALL`
<a id="insn-00bf7fa4"></a> `00bf7fa4` | `c0 00 f8 37` | tbnz w0,#0x1f,0x00bf7fbc | `CONDITIONAL_JUMP`
<a id="insn-00bf7fa8"></a> `00bf7fa8` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-00bf7fac"></a> `00bf7fac` | `bf 02 01 eb` | cmp x21,x1 | `FALL_THROUGH`
<a id="insn-00bf7fb0"></a> `00bf7fb0` | `42 01 00 54` | b.cs 0x00bf7fd8 | `CONDITIONAL_JUMP`
<a id="insn-00bf7fb4"></a> `00bf7fb4` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bf7fb8"></a> `00bf7fb8` | `02 00 00 14` | b 0x00bf7fc0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf7fbc"></a> `00bf7fbc` | `f5 06 15 aa` | orr x21,x23,x21, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00bf7fc0"></a> `00bf7fc0` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bf7fc4"></a> `00bf7fc4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bf7fc8"></a> `00bf7fc8` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00bf7fcc"></a> `00bf7fcc` | `31 8a 01 94` | bl 0x00c5a890 | `UNCONDITIONAL_CALL`
<a id="insn-00bf7fd0"></a> `00bf7fd0` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00bf7fd4"></a> `00bf7fd4` | `ed ff ff 17` | b 0x00bf7f88 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf7fd8"></a> `00bf7fd8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bf7fdc"></a> `00bf7fdc` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00bf7fe0"></a> `00bf7fe0` | `2c 8a 01 94` | bl 0x00c5a890 | `UNCONDITIONAL_CALL`
<a id="insn-00bf7fe4"></a> `00bf7fe4` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00bf7fe8"></a> `00bf7fe8` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf7fec"></a> `00bf7fec` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bf7ff0"></a> `00bf7ff0` | `ff ff 00 a9` | stp xzr,xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bf7ff4"></a> `00bf7ff4` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00bf7ff8"></a> `00bf7ff8` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bf7ffc"></a> `00bf7ffc` | `ff 03 00 f9` | str xzr,[sp] | `FALL_THROUGH`
<a id="insn-00bf8000"></a> `00bf8000` | `48 98 01 94` | bl 0x00c5e120 | `UNCONDITIONAL_CALL`
<a id="insn-00bf8004"></a> `00bf8004` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bf8008"></a> `00bf8008` | `f7 1f 40 f9` | ldr x23,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bf800c"></a> `00bf800c` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bf8010"></a> `00bf8010` | `e8 13 40 fd` | ldr d8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf8014"></a> `00bf8014` | `fd fb 42 a9` | ldp x29,x30,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bf8018"></a> `00bf8018` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bf801c"></a> `00bf801c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf8020"></a> `00bf8020` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf7efc`](#insn-00bf7efc) 範囲 `[['00bf7efc', '00bf7f87']]`
  - `FALL_THROUGH` [`00bf7f84`](#insn-00bf7f84) → [`00bf7f88`](#insn-00bf7f88)
- ブロック [`00bf7f88`](#insn-00bf7f88) 範囲 `[['00bf7f88', '00bf7fa7']]`
  - `CONDITIONAL_JUMP` [`00bf7fa4`](#insn-00bf7fa4) → [`00bf7fbc`](#insn-00bf7fbc)
  - `FALL_THROUGH` [`00bf7fa4`](#insn-00bf7fa4) → [`00bf7fa8`](#insn-00bf7fa8)
- ブロック [`00bf7fa8`](#insn-00bf7fa8) 範囲 `[['00bf7fa8', '00bf7fb3']]`
  - `CONDITIONAL_JUMP` [`00bf7fb0`](#insn-00bf7fb0) → [`00bf7fd8`](#insn-00bf7fd8)
  - `FALL_THROUGH` [`00bf7fb0`](#insn-00bf7fb0) → [`00bf7fb4`](#insn-00bf7fb4)
- ブロック [`00bf7fb4`](#insn-00bf7fb4) 範囲 `[['00bf7fb4', '00bf7fbb']]`
  - `UNCONDITIONAL_JUMP` [`00bf7fb8`](#insn-00bf7fb8) → [`00bf7fc0`](#insn-00bf7fc0)
- ブロック [`00bf7fbc`](#insn-00bf7fbc) 範囲 `[['00bf7fbc', '00bf7fbf']]`
  - `FALL_THROUGH` [`00bf7fbc`](#insn-00bf7fbc) → [`00bf7fc0`](#insn-00bf7fc0)
- ブロック [`00bf7fc0`](#insn-00bf7fc0) 範囲 `[['00bf7fc0', '00bf7fd7']]`
  - `UNCONDITIONAL_JUMP` [`00bf7fd4`](#insn-00bf7fd4) → [`00bf7f88`](#insn-00bf7f88)
- ブロック [`00bf7fd8`](#insn-00bf7fd8) 範囲 `[['00bf7fd8', '00bf8023']]`

## 命令位置別の参照

- [`00bf7f04`](#insn-00bf7f04) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7f08`](#insn-00bf7f08) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7f0c`](#insn-00bf7f0c) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7f10`](#insn-00bf7f10) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7f14`](#insn-00bf7f14) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7f28`](#insn-00bf7f28) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bf7f34`](#insn-00bf7f34) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7f38`](#insn-00bf7f38) → `002c3280`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7f40`](#insn-00bf7f40) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7f60`](#insn-00bf7f60) → [`00c5a890`](../00c5a/00c5a890.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a890` · 推定シンボル `None` · 推定型 `None`
- [`00bf7f64`](#insn-00bf7f64) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7f68`](#insn-00bf7f68) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7f88`](#insn-00bf7f88) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7f9c`](#insn-00bf7f9c) → `003104f4`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7fa0`](#insn-00bf7fa0) → [`00c5e110`](../00c5e/00c5e110.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e110` · 推定シンボル `None` · 推定型 `None`
- [`00bf7fa4`](#insn-00bf7fa4) → [`00bf7fbc`](#insn-00bf7fbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7fb0`](#insn-00bf7fb0) → [`00bf7fd8`](#insn-00bf7fd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7fb8`](#insn-00bf7fb8) → [`00bf7fc0`](#insn-00bf7fc0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7fcc`](#insn-00bf7fcc) → [`00c5a890`](../00c5a/00c5a890.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a890` · 推定シンボル `None` · 推定型 `None`
- [`00bf7fd0`](#insn-00bf7fd0) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7fd4`](#insn-00bf7fd4) → [`00bf7f88`](#insn-00bf7f88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7fe0`](#insn-00bf7fe0) → [`00c5a890`](../00c5a/00c5a890.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a890` · 推定シンボル `None` · 推定型 `None`
- [`00bf7fe4`](#insn-00bf7fe4) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7fe8`](#insn-00bf7fe8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7ff0`](#insn-00bf7ff0) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7ffc`](#insn-00bf7ffc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf8000`](#insn-00bf8000) → [`00c5e120`](../00c5e/00c5e120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e120` · 推定シンボル `None` · 推定型 `None`
- [`00bf8004`](#insn-00bf8004) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf8008`](#insn-00bf8008) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf800c`](#insn-00bf800c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf8010`](#insn-00bf8010) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf8014`](#insn-00bf8014) → `Stack[-0x38]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf7f04`](#insn-00bf7f04)

~~~json
{
  "source": "00bf7f04",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7f08`](#insn-00bf7f08)

~~~json
{
  "source": "00bf7f08",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7f0c`](#insn-00bf7f0c)

~~~json
{
  "source": "00bf7f0c",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7f10`](#insn-00bf7f10)

~~~json
{
  "source": "00bf7f10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7f14`](#insn-00bf7f14)

~~~json
{
  "source": "00bf7f14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7f28`](#insn-00bf7f28)

~~~json
{
  "source": "00bf7f28",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf7f34`](#insn-00bf7f34)

~~~json
{
  "source": "00bf7f34",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7f38`](#insn-00bf7f38)

~~~json
{
  "source": "00bf7f38",
  "target": "002c3280",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7f40`](#insn-00bf7f40)

~~~json
{
  "source": "00bf7f40",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7f60`](#insn-00bf7f60)

~~~json
{
  "source": "00bf7f60",
  "target": "00c5a890",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf7f64`](#insn-00bf7f64)

~~~json
{
  "source": "00bf7f64",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7f68`](#insn-00bf7f68)

~~~json
{
  "source": "00bf7f68",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7f88`](#insn-00bf7f88)

~~~json
{
  "source": "00bf7f88",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7f9c`](#insn-00bf7f9c)

~~~json
{
  "source": "00bf7f9c",
  "target": "003104f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7fa0`](#insn-00bf7fa0)

~~~json
{
  "source": "00bf7fa0",
  "target": "00c5e110",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf7fa4`](#insn-00bf7fa4)

~~~json
{
  "source": "00bf7fa4",
  "target": "00bf7fbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7fb0`](#insn-00bf7fb0)

~~~json
{
  "source": "00bf7fb0",
  "target": "00bf7fd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7fb8`](#insn-00bf7fb8)

~~~json
{
  "source": "00bf7fb8",
  "target": "00bf7fc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7fcc`](#insn-00bf7fcc)

~~~json
{
  "source": "00bf7fcc",
  "target": "00c5a890",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf7fd0`](#insn-00bf7fd0)

~~~json
{
  "source": "00bf7fd0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7fd4`](#insn-00bf7fd4)

~~~json
{
  "source": "00bf7fd4",
  "target": "00bf7f88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7fe0`](#insn-00bf7fe0)

~~~json
{
  "source": "00bf7fe0",
  "target": "00c5a890",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf7fe4`](#insn-00bf7fe4)

~~~json
{
  "source": "00bf7fe4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7fe8`](#insn-00bf7fe8)

~~~json
{
  "source": "00bf7fe8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7ff0`](#insn-00bf7ff0)

~~~json
{
  "source": "00bf7ff0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7ffc`](#insn-00bf7ffc)

~~~json
{
  "source": "00bf7ffc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf8000`](#insn-00bf8000)

~~~json
{
  "source": "00bf8000",
  "target": "00c5e120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf8004`](#insn-00bf8004)

~~~json
{
  "source": "00bf8004",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf8008`](#insn-00bf8008)

~~~json
{
  "source": "00bf8008",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf800c`](#insn-00bf800c)

~~~json
{
  "source": "00bf800c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf8010`](#insn-00bf8010)

~~~json
{
  "source": "00bf8010",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf8014`](#insn-00bf8014)

~~~json
{
  "source": "00bf8014",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
