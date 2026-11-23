# 00ad5fec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ad60b4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad60b4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-40db739cb828f53faf30fd3a9ce134aa)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ad5fec",
  "name": "FUN_00ad5fec",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dc0b4deb46a094d3b2167dd44da00a4e15521abe59f996d0a4f839b85dc9e2db",
  "source_text_sha256": "dc0b4deb46a094d3b2167dd44da00a4e15521abe59f996d0a4f839b85dc9e2db",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ad5fec",
        "00ad60ef"
      ]
    ],
    "bytes_sha256": "ccd4e8e5221830f96c0915644ce5c8a25dd95417156f09e9a8491ad207c824ed",
    "instruction_count": 65,
    "instruction_bytes": 260,
    "body_bytes": 260,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ad5e00](../00ad5/00ad5e00.md)

## 呼び出し先

- [00bdb100](../00bdb/00bdb100.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1502 bytes

~~~c

long * FUN_00ad5fec(long param_1,undefined8 *param_2,byte *param_3)

{
  void *__s2;
  size_t __n;
  ulong uVar1;
  byte *__s1;
  bool bVar2;
  ulong uVar3;
  int iVar4;
  long *plVar5;
  long *plVar6;
  long *plVar7;
  
  plVar6 = (long *)(param_1 + 8);
  plVar5 = (long *)*plVar6;
  plVar7 = plVar6;
  if (plVar5 != (long *)0x0) {
    uVar1 = *(ulong *)(param_3 + 8);
    __s1 = *(byte **)(param_3 + 0x10);
    if ((*param_3 & 1) == 0) {
      __s1 = param_3 + 1;
      uVar1 = (ulong)(*param_3 >> 1);
    }
    do {
      while( true ) {
        plVar7 = plVar5;
        __s2 = (void *)((long)plVar7 + 0x21);
        uVar3 = (ulong)(*(byte *)(plVar7 + 4) >> 1);
        if ((*(byte *)(plVar7 + 4) & 1) != 0) {
          __s2 = (void *)plVar7[6];
          uVar3 = plVar7[5];
        }
        __n = uVar3;
        if (uVar1 <= uVar3) {
          __n = uVar1;
        }
        iVar4 = memcmp(__s1,__s2,__n);
        bVar2 = uVar1 < uVar3;
        if (iVar4 != 0) {
          bVar2 = iVar4 < 0;
        }
        if (bVar2) break;
        iVar4 = memcmp(__s2,__s1,__n);
        bVar2 = uVar3 < uVar1;
        if (iVar4 != 0) {
          bVar2 = iVar4 < 0;
        }
        if (!bVar2) goto LAB_00ad60d0;
        plVar6 = plVar7 + 1;
        plVar5 = (long *)*plVar6;
        if ((long *)*plVar6 == (long *)0x0) goto LAB_00ad60d0;
      }
      plVar5 = (long *)*plVar7;
      plVar6 = plVar7;
    } while ((long *)*plVar7 != (long *)0x0);
  }
LAB_00ad60d0:
  *param_2 = plVar7;
  return plVar6;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ad5fec"></a> `00ad5fec` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00ad5ff0"></a> `00ad5ff0` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ad5ff4"></a> `00ad5ff4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ad5ff8"></a> `00ad5ff8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ad5ffc"></a> `00ad5ffc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ad6000"></a> `00ad6000` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ad6004"></a> `00ad6004` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00ad6008"></a> `00ad6008` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00ad600c"></a> `00ad600c` | `88 8e 40 f8` | ldr x8,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00ad6010"></a> `00ad6010` | `e8 05 00 b4` | cbz x8,0x00ad60cc | `CONDITIONAL_JUMP`
<a id="insn-00ad6014"></a> `00ad6014` | `49 00 40 39` | ldrb w9,[x2] | `FALL_THROUGH`
<a id="insn-00ad6018"></a> `00ad6018` | `4b b0 40 a9` | ldp x11,x12,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00ad601c"></a> `00ad601c` | `2a fd 41 d3` | lsr x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00ad6020"></a> `00ad6020` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00ad6024"></a> `00ad6024` | `95 15 82 9a` | csinc x21,x12,x2,ne | `FALL_THROUGH`
<a id="insn-00ad6028"></a> `00ad6028` | `59 01 8b 9a` | csel x25,x10,x11,eq | `FALL_THROUGH`
<a id="insn-00ad602c"></a> `00ad602c` | `04 00 00 14` | b 0x00ad603c | `UNCONDITIONAL_JUMP`
<a id="insn-00ad6030"></a> `00ad6030` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00ad6034"></a> `00ad6034` | `f4 03 18 aa` | mov x20,x24 | `FALL_THROUGH`
<a id="insn-00ad6038"></a> `00ad6038` | `c8 04 00 b4` | cbz x8,0x00ad60d0 | `CONDITIONAL_JUMP`
<a id="insn-00ad603c"></a> `00ad603c` | `f8 03 08 aa` | mov x24,x8 | `FALL_THROUGH`
<a id="insn-00ad6040"></a> `00ad6040` | `08 81 40 39` | ldrb w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00ad6044"></a> `00ad6044` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ad6048"></a> `00ad6048` | `09 af 42 a9` | ldp x9,x11,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00ad604c"></a> `00ad604c` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ad6050"></a> `00ad6050` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ad6054"></a> `00ad6054` | `08 87 00 91` | add x8,x24,#0x21 | `FALL_THROUGH`
<a id="insn-00ad6058"></a> `00ad6058` | `5a 01 89 9a` | csel x26,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00ad605c"></a> `00ad605c` | `16 01 8b 9a` | csel x22,x8,x11,eq | `FALL_THROUGH`
<a id="insn-00ad6060"></a> `00ad6060` | `5f 03 19 eb` | cmp x26,x25 | `FALL_THROUGH`
<a id="insn-00ad6064"></a> `00ad6064` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00ad6068"></a> `00ad6068` | `57 33 99 9a` | csel x23,x26,x25,cc | `FALL_THROUGH`
<a id="insn-00ad606c"></a> `00ad606c` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00ad6070"></a> `00ad6070` | `24 14 04 94` | bl 0x00bdb100 | `UNCONDITIONAL_CALL`
<a id="insn-00ad6074"></a> `00ad6074` | `3f 03 1a eb` | cmp x25,x26 | `FALL_THROUGH`
<a id="insn-00ad6078"></a> `00ad6078` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00ad607c"></a> `00ad607c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00ad6080"></a> `00ad6080` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00ad6084"></a> `00ad6084` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00ad6088"></a> `00ad6088` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ad608c"></a> `00ad608c` | `20 fd ff 54` | b.eq 0x00ad6030 | `CONDITIONAL_JUMP`
<a id="insn-00ad6090"></a> `00ad6090` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00ad6094"></a> `00ad6094` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ad6098"></a> `00ad6098` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00ad609c"></a> `00ad609c` | `19 14 04 94` | bl 0x00bdb100 | `UNCONDITIONAL_CALL`
<a id="insn-00ad60a0"></a> `00ad60a0` | `5f 03 19 eb` | cmp x26,x25 | `FALL_THROUGH`
<a id="insn-00ad60a4"></a> `00ad60a4` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00ad60a8"></a> `00ad60a8` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00ad60ac"></a> `00ad60ac` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00ad60b0"></a> `00ad60b0` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00ad60b4"></a> `00ad60b4` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ad60b8"></a> `00ad60b8` | `c1 00 00 54` | b.ne 0x00ad60d0 | `CONDITIONAL_JUMP`
<a id="insn-00ad60bc"></a> `00ad60bc` | `f4 03 18 aa` | mov x20,x24 | `FALL_THROUGH`
<a id="insn-00ad60c0"></a> `00ad60c0` | `88 8e 40 f8` | ldr x8,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00ad60c4"></a> `00ad60c4` | `c8 fb ff b5` | cbnz x8,0x00ad603c | `CONDITIONAL_JUMP`
<a id="insn-00ad60c8"></a> `00ad60c8` | `02 00 00 14` | b 0x00ad60d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad60cc"></a> `00ad60cc` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00ad60d0"></a> `00ad60d0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ad60d4"></a> `00ad60d4` | `78 02 00 f9` | str x24,[x19] | `FALL_THROUGH`
<a id="insn-00ad60d8"></a> `00ad60d8` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ad60dc"></a> `00ad60dc` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ad60e0"></a> `00ad60e0` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ad60e4"></a> `00ad60e4` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ad60e8"></a> `00ad60e8` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00ad60ec"></a> `00ad60ec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ad5fec`](#insn-00ad5fec) 範囲 `[['00ad5fec', '00ad6013']]`
  - `CONDITIONAL_JUMP` [`00ad6010`](#insn-00ad6010) → [`00ad60cc`](#insn-00ad60cc)
  - `FALL_THROUGH` [`00ad6010`](#insn-00ad6010) → [`00ad6014`](#insn-00ad6014)
- ブロック [`00ad6014`](#insn-00ad6014) 範囲 `[['00ad6014', '00ad602f']]`
  - `UNCONDITIONAL_JUMP` [`00ad602c`](#insn-00ad602c) → [`00ad603c`](#insn-00ad603c)
- ブロック [`00ad6030`](#insn-00ad6030) 範囲 `[['00ad6030', '00ad603b']]`
  - `CONDITIONAL_JUMP` [`00ad6038`](#insn-00ad6038) → [`00ad60d0`](#insn-00ad60d0)
  - `FALL_THROUGH` [`00ad6038`](#insn-00ad6038) → [`00ad603c`](#insn-00ad603c)
- ブロック [`00ad603c`](#insn-00ad603c) 範囲 `[['00ad603c', '00ad608f']]`
  - `CONDITIONAL_JUMP` [`00ad608c`](#insn-00ad608c) → [`00ad6030`](#insn-00ad6030)
  - `FALL_THROUGH` [`00ad608c`](#insn-00ad608c) → [`00ad6090`](#insn-00ad6090)
- ブロック [`00ad6090`](#insn-00ad6090) 範囲 `[['00ad6090', '00ad60bb']]`
  - `CONDITIONAL_JUMP` [`00ad60b8`](#insn-00ad60b8) → [`00ad60d0`](#insn-00ad60d0)
  - `FALL_THROUGH` [`00ad60b8`](#insn-00ad60b8) → [`00ad60bc`](#insn-00ad60bc)
- ブロック [`00ad60bc`](#insn-00ad60bc) 範囲 `[['00ad60bc', '00ad60c7']]`
  - `CONDITIONAL_JUMP` [`00ad60c4`](#insn-00ad60c4) → [`00ad603c`](#insn-00ad603c)
  - `FALL_THROUGH` [`00ad60c4`](#insn-00ad60c4) → [`00ad60c8`](#insn-00ad60c8)
- ブロック [`00ad60c8`](#insn-00ad60c8) 範囲 `[['00ad60c8', '00ad60cb']]`
  - `UNCONDITIONAL_JUMP` [`00ad60c8`](#insn-00ad60c8) → [`00ad60d0`](#insn-00ad60d0)
- ブロック [`00ad60cc`](#insn-00ad60cc) 範囲 `[['00ad60cc', '00ad60cf']]`
  - `FALL_THROUGH` [`00ad60cc`](#insn-00ad60cc) → [`00ad60d0`](#insn-00ad60d0)
- ブロック [`00ad60d0`](#insn-00ad60d0) 範囲 `[['00ad60d0', '00ad60ef']]`

## 命令位置別の参照

- [`00ad5fec`](#insn-00ad5fec) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad5ff0`](#insn-00ad5ff0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad5ff4`](#insn-00ad5ff4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad5ff8`](#insn-00ad5ff8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad5ffc`](#insn-00ad5ffc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6010`](#insn-00ad6010) → [`00ad60cc`](#insn-00ad60cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad602c`](#insn-00ad602c) → [`00ad603c`](#insn-00ad603c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6038`](#insn-00ad6038) → [`00ad60d0`](#insn-00ad60d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6070`](#insn-00ad6070) → [`00bdb100`](../00bdb/00bdb100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb100` · 推定シンボル `None` · 推定型 `None`
- [`00ad608c`](#insn-00ad608c) → [`00ad6030`](#insn-00ad6030) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad609c`](#insn-00ad609c) → [`00bdb100`](../00bdb/00bdb100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb100` · 推定シンボル `None` · 推定型 `None`
- [`00ad60b8`](#insn-00ad60b8) → [`00ad60d0`](#insn-00ad60d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad60c4`](#insn-00ad60c4) → [`00ad603c`](#insn-00ad603c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad60c8`](#insn-00ad60c8) → [`00ad60d0`](#insn-00ad60d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad60d8`](#insn-00ad60d8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad60dc`](#insn-00ad60dc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad60e0`](#insn-00ad60e0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad60e4`](#insn-00ad60e4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad60e8`](#insn-00ad60e8) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ad5fec`](#insn-00ad5fec)

~~~json
{
  "source": "00ad5fec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad5ff0`](#insn-00ad5ff0)

~~~json
{
  "source": "00ad5ff0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad5ff4`](#insn-00ad5ff4)

~~~json
{
  "source": "00ad5ff4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad5ff8`](#insn-00ad5ff8)

~~~json
{
  "source": "00ad5ff8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad5ffc`](#insn-00ad5ffc)

~~~json
{
  "source": "00ad5ffc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6010`](#insn-00ad6010)

~~~json
{
  "source": "00ad6010",
  "target": "00ad60cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad602c`](#insn-00ad602c)

~~~json
{
  "source": "00ad602c",
  "target": "00ad603c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6038`](#insn-00ad6038)

~~~json
{
  "source": "00ad6038",
  "target": "00ad60d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6070`](#insn-00ad6070)

~~~json
{
  "source": "00ad6070",
  "target": "00bdb100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad608c`](#insn-00ad608c)

~~~json
{
  "source": "00ad608c",
  "target": "00ad6030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad609c`](#insn-00ad609c)

~~~json
{
  "source": "00ad609c",
  "target": "00bdb100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad60b8`](#insn-00ad60b8)

~~~json
{
  "source": "00ad60b8",
  "target": "00ad60d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad60c4`](#insn-00ad60c4)

~~~json
{
  "source": "00ad60c4",
  "target": "00ad603c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad60c8`](#insn-00ad60c8)

~~~json
{
  "source": "00ad60c8",
  "target": "00ad60d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad60d8`](#insn-00ad60d8)

~~~json
{
  "source": "00ad60d8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad60dc`](#insn-00ad60dc)

~~~json
{
  "source": "00ad60dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad60e0`](#insn-00ad60e0)

~~~json
{
  "source": "00ad60e0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad60e4`](#insn-00ad60e4)

~~~json
{
  "source": "00ad60e4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad60e8`](#insn-00ad60e8)

~~~json
{
  "source": "00ad60e8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
