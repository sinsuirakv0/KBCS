# 00aeffd8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aefbb0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefbb0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0065.md#compare-e6915e6ffe7492f8369a565a82b91541)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00af0074`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0074.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0066.md#compare-265fffff6c560e1d93a6bd53e971d801)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeffd8",
  "name": "FUN_00aeffd8",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "46e24b343e6ee9cea11cdfd59c0ee312d51c517d37de9f0c5147adb5b65cef0c",
  "source_text_sha256": "46e24b343e6ee9cea11cdfd59c0ee312d51c517d37de9f0c5147adb5b65cef0c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeffd8",
        "00af008b"
      ]
    ],
    "bytes_sha256": "311e871441ecda8d28c89fefd15a82b54bc8e1c20a4d0e408551fb278b5e9e34",
    "instruction_count": 45,
    "instruction_bytes": 180,
    "body_bytes": 180,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [008b6f50](../008b6/008b6f50.md)
- [00b0b640](../00b0b/00b0b640.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 760 bytes

~~~c

void FUN_00aeffd8(long param_1,undefined8 *param_2,int *param_3)

{
  int iVar1;
  undefined8 uVar2;
  ulong uVar3;
  undefined4 uVar4;
  undefined8 uVar5;
  long lVar6;
  
  iVar1 = *param_3;
  uVar5 = *param_2;
  if (iVar1 == 4) {
    lVar6 = *(long *)(param_1 + 8);
    uVar3 = FUN_008b6f50(uVar5);
    if ((uVar3 & 1) == 0) {
      return;
    }
    FUN_00b0b640(lVar6 + 0x3d8,*(long *)(param_1 + 0x10),*(long *)(param_1 + 0x10) + 0x510,0);
    return;
  }
  if (iVar1 == 3) {
    uVar2 = FUN_0047acf4();
    uVar3 = FUN_008b6f50(uVar5);
    uVar4 = 0xb;
    if ((uVar3 & 1) == 0) {
      uVar4 = 0xf;
    }
  }
  else {
    if (iVar1 != 0) {
      return;
    }
    uVar2 = FUN_0047acf4();
    uVar4 = 10;
  }
  FUN_0047cdd4(uVar2,uVar4,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeffd8"></a> `00aeffd8` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aeffdc"></a> `00aeffdc` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeffe0"></a> `00aeffe0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeffe4"></a> `00aeffe4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aeffe8"></a> `00aeffe8` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00aeffec"></a> `00aeffec` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-00aefff0"></a> `00aefff0` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00aefff4"></a> `00aefff4` | `a0 02 00 54` | b.eq 0x00af0048 | `CONDITIONAL_JUMP`
<a id="insn-00aefff8"></a> `00aefff8` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00aefffc"></a> `00aefffc` | `a0 00 00 54` | b.eq 0x00af0010 | `CONDITIONAL_JUMP`
<a id="insn-00af0000"></a> `00af0000` | `e8 03 00 35` | cbnz w8,0x00af007c | `CONDITIONAL_JUMP`
<a id="insn-00af0004"></a> `00af0004` | `3c 2b e6 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-00af0008"></a> `00af0008` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00af000c"></a> `00af000c` | `0a 00 00 14` | b 0x00af0034 | `UNCONDITIONAL_JUMP`
<a id="insn-00af0010"></a> `00af0010` | `39 2b e6 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-00af0014"></a> `00af0014` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00af0018"></a> `00af0018` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af001c"></a> `00af001c` | `cd 1b f7 97` | bl 0x008b6f50 | `UNCONDITIONAL_CALL`
<a id="insn-00af0020"></a> `00af0020` | `e8 01 80 52` | mov w8,#0xf | `FALL_THROUGH`
<a id="insn-00af0024"></a> `00af0024` | `1f 00 00 72` | tst w0,#0x1 | `FALL_THROUGH`
<a id="insn-00af0028"></a> `00af0028` | `69 01 80 52` | mov w9,#0xb | `FALL_THROUGH`
<a id="insn-00af002c"></a> `00af002c` | `21 11 88 1a` | csel w1,w9,w8,ne | `FALL_THROUGH`
<a id="insn-00af0030"></a> `00af0030` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00af0034"></a> `00af0034` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00af0038"></a> `00af0038` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af003c"></a> `00af003c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af0040"></a> `00af0040` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00af0044"></a> `00af0044` | `64 33 e6 17` | b 0x0047cdd4 | `CALL_TERMINATOR`
<a id="insn-00af0048"></a> `00af0048` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00af004c"></a> `00af004c` | `14 04 40 f9` | ldr x20,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00af0050"></a> `00af0050` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af0054"></a> `00af0054` | `bf 1b f7 97` | bl 0x008b6f50 | `UNCONDITIONAL_CALL`
<a id="insn-00af0058"></a> `00af0058` | `20 01 00 36` | tbz w0,#0x0,0x00af007c | `CONDITIONAL_JUMP`
<a id="insn-00af005c"></a> `00af005c` | `a1 0a 40 f9` | ldr x1,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00af0060"></a> `00af0060` | `80 62 0f 91` | add x0,x20,#0x3d8 | `FALL_THROUGH`
<a id="insn-00af0064"></a> `00af0064` | `22 40 14 91` | add x2,x1,#0x510 | `FALL_THROUGH`
<a id="insn-00af0068"></a> `00af0068` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00af006c"></a> `00af006c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af0070"></a> `00af0070` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af0074"></a> `00af0074` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00af0078"></a> `00af0078` | `72 6d 00 14` | b 0x00b0b640 | `CALL_TERMINATOR`
<a id="insn-00af007c"></a> `00af007c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af0080"></a> `00af0080` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af0084"></a> `00af0084` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00af0088"></a> `00af0088` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeffd8`](#insn-00aeffd8) 範囲 `[['00aeffd8', '00aefff7']]`
  - `CONDITIONAL_JUMP` [`00aefff4`](#insn-00aefff4) → [`00af0048`](#insn-00af0048)
  - `FALL_THROUGH` [`00aefff4`](#insn-00aefff4) → [`00aefff8`](#insn-00aefff8)
- ブロック [`00aefff8`](#insn-00aefff8) 範囲 `[['00aefff8', '00aeffff']]`
  - `CONDITIONAL_JUMP` [`00aefffc`](#insn-00aefffc) → [`00af0010`](#insn-00af0010)
  - `FALL_THROUGH` [`00aefffc`](#insn-00aefffc) → [`00af0000`](#insn-00af0000)
- ブロック [`00af0000`](#insn-00af0000) 範囲 `[['00af0000', '00af0003']]`
  - `CONDITIONAL_JUMP` [`00af0000`](#insn-00af0000) → [`00af007c`](#insn-00af007c)
  - `FALL_THROUGH` [`00af0000`](#insn-00af0000) → [`00af0004`](#insn-00af0004)
- ブロック [`00af0004`](#insn-00af0004) 範囲 `[['00af0004', '00af000f']]`
  - `UNCONDITIONAL_JUMP` [`00af000c`](#insn-00af000c) → [`00af0034`](#insn-00af0034)
- ブロック [`00af0010`](#insn-00af0010) 範囲 `[['00af0010', '00af0033']]`
  - `FALL_THROUGH` [`00af0030`](#insn-00af0030) → [`00af0034`](#insn-00af0034)
- ブロック [`00af0034`](#insn-00af0034) 範囲 `[['00af0034', '00af0047']]`
- ブロック [`00af0048`](#insn-00af0048) 範囲 `[['00af0048', '00af005b']]`
  - `CONDITIONAL_JUMP` [`00af0058`](#insn-00af0058) → [`00af007c`](#insn-00af007c)
  - `FALL_THROUGH` [`00af0058`](#insn-00af0058) → [`00af005c`](#insn-00af005c)
- ブロック [`00af005c`](#insn-00af005c) 範囲 `[['00af005c', '00af007b']]`
- ブロック [`00af007c`](#insn-00af007c) 範囲 `[['00af007c', '00af008b']]`

## 命令位置別の参照

- [`00aeffd8`](#insn-00aeffd8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeffdc`](#insn-00aeffdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeffe0`](#insn-00aeffe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefff4`](#insn-00aefff4) → [`00af0048`](#insn-00af0048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefffc`](#insn-00aefffc) → [`00af0010`](#insn-00af0010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0000`](#insn-00af0000) → [`00af007c`](#insn-00af007c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0004`](#insn-00af0004) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`00af000c`](#insn-00af000c) → [`00af0034`](#insn-00af0034) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0010`](#insn-00af0010) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`00af001c`](#insn-00af001c) → [`008b6f50`](../008b6/008b6f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6f50` · 推定シンボル `None` · 推定型 `None`
- [`00af0038`](#insn-00af0038) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af003c`](#insn-00af003c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0040`](#insn-00af0040) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0044`](#insn-00af0044) → [`0047cdd4`](../0047c/0047cdd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cdd4` · 推定シンボル `None` · 推定型 `None`
- [`00af0054`](#insn-00af0054) → [`008b6f50`](../008b6/008b6f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6f50` · 推定シンボル `None` · 推定型 `None`
- [`00af0058`](#insn-00af0058) → [`00af007c`](#insn-00af007c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af006c`](#insn-00af006c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0070`](#insn-00af0070) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0074`](#insn-00af0074) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0078`](#insn-00af0078) → [`00b0b640`](../00b0b/00b0b640.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b0b640` · 推定シンボル `None` · 推定型 `None`
- [`00af007c`](#insn-00af007c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0080`](#insn-00af0080) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0084`](#insn-00af0084) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeffd8`](#insn-00aeffd8)

~~~json
{
  "source": "00aeffd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeffdc`](#insn-00aeffdc)

~~~json
{
  "source": "00aeffdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeffe0`](#insn-00aeffe0)

~~~json
{
  "source": "00aeffe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefff4`](#insn-00aefff4)

~~~json
{
  "source": "00aefff4",
  "target": "00af0048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefffc`](#insn-00aefffc)

~~~json
{
  "source": "00aefffc",
  "target": "00af0010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0000`](#insn-00af0000)

~~~json
{
  "source": "00af0000",
  "target": "00af007c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0004`](#insn-00af0004)

~~~json
{
  "source": "00af0004",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af000c`](#insn-00af000c)

~~~json
{
  "source": "00af000c",
  "target": "00af0034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0010`](#insn-00af0010)

~~~json
{
  "source": "00af0010",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af001c`](#insn-00af001c)

~~~json
{
  "source": "00af001c",
  "target": "008b6f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0038`](#insn-00af0038)

~~~json
{
  "source": "00af0038",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af003c`](#insn-00af003c)

~~~json
{
  "source": "00af003c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0040`](#insn-00af0040)

~~~json
{
  "source": "00af0040",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0044`](#insn-00af0044)

~~~json
{
  "source": "00af0044",
  "target": "0047cdd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0054`](#insn-00af0054)

~~~json
{
  "source": "00af0054",
  "target": "008b6f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0058`](#insn-00af0058)

~~~json
{
  "source": "00af0058",
  "target": "00af007c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af006c`](#insn-00af006c)

~~~json
{
  "source": "00af006c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0070`](#insn-00af0070)

~~~json
{
  "source": "00af0070",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0074`](#insn-00af0074)

~~~json
{
  "source": "00af0074",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0078`](#insn-00af0078)

~~~json
{
  "source": "00af0078",
  "target": "00b0b640",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af007c`](#insn-00af007c)

~~~json
{
  "source": "00af007c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0080`](#insn-00af0080)

~~~json
{
  "source": "00af0080",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0084`](#insn-00af0084)

~~~json
{
  "source": "00af0084",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
