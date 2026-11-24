# 00afeea4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0170.md#review-3999e91f3ae0395230de6aca3530d19f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aff2cc`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aff/00aff2cc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0066.md#compare-a4d620983c1b7bba5dfb5fc2f72033b1)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afeea4",
  "name": "FUN_00afeea4",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ef94e68cb2274b07dfacb13469e1a75dd5b860b0bf142f011ef0f5f48abbfe64",
  "source_text_sha256": "ef94e68cb2274b07dfacb13469e1a75dd5b860b0bf142f011ef0f5f48abbfe64",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afeea4",
        "00afef73"
      ]
    ],
    "bytes_sha256": "80dc92162b10366d6383d6954da9002da7c9ba6e71e7bb1f87e6fdd35c60db85",
    "instruction_count": 52,
    "instruction_bytes": 208,
    "body_bytes": 208,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00685548](../00685/00685548.md)
- [006c52b8](../006c5/006c52b8.md)
- [00a4f1bc](../00a4f/00a4f1bc.md)
- [00af566c](../00af5/00af566c.md)
- [00b005b4](../00b00/00b005b4.md)

## 呼び出し先

- [005e73e0](../005e7/005e73e0.md)
- [008514b8](../00851/008514b8.md)
- [00b04854](../00b04/00b04854.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 662 bytes

~~~c

ulong FUN_00afeea4(int param_1,int param_2,int param_3,ulong param_4)

{
  int iVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_008514b8();
  uVar3 = FUN_005e73e0(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  lVar2 = FUN_008514b8();
  if ((uVar3 & 1) == 0) {
    uVar3 = (ulong)(*(int *)((long)__DT_JMPREL + lVar2 + ((long)param_2 + 2) * 0x1c4 + 0x1840) != 0)
    ;
  }
  else {
    iVar1 = *(int *)(lVar2 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f724);
    uVar3 = (ulong)(iVar1 != 0);
    if ((iVar1 == 0) && ((param_4 & 1) != 0)) {
      uVar3 = FUN_00b04854(param_1,param_2,param_3,0x20);
      return uVar3;
    }
  }
  return uVar3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afeea4"></a> `00afeea4` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00afeea8"></a> `00afeea8` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afeeac"></a> `00afeeac` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afeeb0"></a> `00afeeb0` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afeeb4"></a> `00afeeb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afeeb8"></a> `00afeeb8` | `f6 03 03 2a` | mov w22,w3 | `FALL_THROUGH`
<a id="insn-00afeebc"></a> `00afeebc` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00afeec0"></a> `00afeec0` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00afeec4"></a> `00afeec4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afeec8"></a> `00afeec8` | `7c 49 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afeecc"></a> `00afeecc` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afeed0"></a> `00afeed0` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afeed4"></a> `00afeed4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afeed8"></a> `00afeed8` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afeedc"></a> `00afeedc` | `41 a1 eb 97` | bl 0x005e73e0 | `UNCONDITIONAL_CALL`
<a id="insn-00afeee0"></a> `00afeee0` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00afeee4"></a> `00afeee4` | `75 49 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afeee8"></a> `00afeee8` | `88 7e 40 93` | sxtw x8,w20 | `FALL_THROUGH`
<a id="insn-00afeeec"></a> `00afeeec` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00afeef0"></a> `00afeef0` | `b7 01 00 37` | tbnz w23,#0x0,0x00afef24 | `CONDITIONAL_JUMP`
<a id="insn-00afeef4"></a> `00afeef4` | `89 38 80 52` | mov w9,#0x1c4 | `FALL_THROUGH`
<a id="insn-00afeef8"></a> `00afeef8` | `08 01 09 9b` | madd x8,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00afeefc"></a> `00afeefc` | `09 5b 9a 52` | mov w9,#0xd2d8 | `FALL_THROUGH`
<a id="insn-00afef00"></a> `00afef00` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00afef04"></a> `00afef04` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afef08"></a> `00afef08` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00afef0c"></a> `00afef0c` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00afef10"></a> `00afef10` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afef14"></a> `00afef14` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afef18"></a> `00afef18` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afef1c"></a> `00afef1c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00afef20"></a> `00afef20` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afef24"></a> `00afef24` | `09 ee 80 52` | mov w9,#0x770 | `FALL_THROUGH`
<a id="insn-00afef28"></a> `00afef28` | `08 01 09 9b` | madd x8,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00afef2c"></a> `00afef2c` | `89 3b 80 52` | mov w9,#0x1dc | `FALL_THROUGH`
<a id="insn-00afef30"></a> `00afef30` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afef34"></a> `00afef34` | `89 e4 9e 52` | mov w9,#0xf724 | `FALL_THROUGH`
<a id="insn-00afef38"></a> `00afef38` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00afef3c"></a> `00afef3c` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afef40"></a> `00afef40` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00afef44"></a> `00afef44` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00afef48"></a> `00afef48` | `48 fe ff 35` | cbnz w8,0x00afef10 | `CONDITIONAL_JUMP`
<a id="insn-00afef4c"></a> `00afef4c` | `36 fe 07 36` | tbz w22,#0x0,0x00afef10 | `CONDITIONAL_JUMP`
<a id="insn-00afef50"></a> `00afef50` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00afef54"></a> `00afef54` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00afef58"></a> `00afef58` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00afef5c"></a> `00afef5c` | `03 04 80 52` | mov w3,#0x20 | `FALL_THROUGH`
<a id="insn-00afef60"></a> `00afef60` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afef64"></a> `00afef64` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afef68"></a> `00afef68` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afef6c"></a> `00afef6c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00afef70"></a> `00afef70` | `39 16 00 14` | b 0x00b04854 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afeea4`](#insn-00afeea4) 範囲 `[['00afeea4', '00afeef3']]`
  - `CONDITIONAL_JUMP` [`00afeef0`](#insn-00afeef0) → [`00afef24`](#insn-00afef24)
  - `FALL_THROUGH` [`00afeef0`](#insn-00afeef0) → [`00afeef4`](#insn-00afeef4)
- ブロック [`00afeef4`](#insn-00afeef4) 範囲 `[['00afeef4', '00afef0f']]`
  - `FALL_THROUGH` [`00afef0c`](#insn-00afef0c) → [`00afef10`](#insn-00afef10)
- ブロック [`00afef10`](#insn-00afef10) 範囲 `[['00afef10', '00afef23']]`
- ブロック [`00afef24`](#insn-00afef24) 範囲 `[['00afef24', '00afef4b']]`
  - `CONDITIONAL_JUMP` [`00afef48`](#insn-00afef48) → [`00afef10`](#insn-00afef10)
  - `FALL_THROUGH` [`00afef48`](#insn-00afef48) → [`00afef4c`](#insn-00afef4c)
- ブロック [`00afef4c`](#insn-00afef4c) 範囲 `[['00afef4c', '00afef4f']]`
  - `CONDITIONAL_JUMP` [`00afef4c`](#insn-00afef4c) → [`00afef10`](#insn-00afef10)
  - `FALL_THROUGH` [`00afef4c`](#insn-00afef4c) → [`00afef50`](#insn-00afef50)
- ブロック [`00afef50`](#insn-00afef50) 範囲 `[['00afef50', '00afef73']]`

## 命令位置別の参照

- [`00afeea4`](#insn-00afeea4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeea8`](#insn-00afeea8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeeac`](#insn-00afeeac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeeb0`](#insn-00afeeb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeec8`](#insn-00afeec8) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afeedc`](#insn-00afeedc) → [`005e73e0`](../005e7/005e73e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e73e0` · 推定シンボル `None` · 推定型 `None`
- [`00afeee4`](#insn-00afeee4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afeef0`](#insn-00afeef0) → [`00afef24`](#insn-00afef24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef04`](#insn-00afef04) → `0023d2d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afef10`](#insn-00afef10) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef14`](#insn-00afef14) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef18`](#insn-00afef18) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef1c`](#insn-00afef1c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef48`](#insn-00afef48) → [`00afef10`](#insn-00afef10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef4c`](#insn-00afef4c) → [`00afef10`](#insn-00afef10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef60`](#insn-00afef60) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef64`](#insn-00afef64) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef68`](#insn-00afef68) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef6c`](#insn-00afef6c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef70`](#insn-00afef70) → [`00b04854`](../00b04/00b04854.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b04854` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afeea4`](#insn-00afeea4)

~~~json
{
  "source": "00afeea4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeea8`](#insn-00afeea8)

~~~json
{
  "source": "00afeea8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeeac`](#insn-00afeeac)

~~~json
{
  "source": "00afeeac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeeb0`](#insn-00afeeb0)

~~~json
{
  "source": "00afeeb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeec8`](#insn-00afeec8)

~~~json
{
  "source": "00afeec8",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afeedc`](#insn-00afeedc)

~~~json
{
  "source": "00afeedc",
  "target": "005e73e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afeee4`](#insn-00afeee4)

~~~json
{
  "source": "00afeee4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afeef0`](#insn-00afeef0)

~~~json
{
  "source": "00afeef0",
  "target": "00afef24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef04`](#insn-00afef04)

~~~json
{
  "source": "00afef04",
  "target": "0023d2d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6208,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0bab9000000000002040000010000000000000000000000d8bab90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afef10`](#insn-00afef10)

~~~json
{
  "source": "00afef10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef14`](#insn-00afef14)

~~~json
{
  "source": "00afef14",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef18`](#insn-00afef18)

~~~json
{
  "source": "00afef18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef1c`](#insn-00afef1c)

~~~json
{
  "source": "00afef1c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef48`](#insn-00afef48)

~~~json
{
  "source": "00afef48",
  "target": "00afef10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef4c`](#insn-00afef4c)

~~~json
{
  "source": "00afef4c",
  "target": "00afef10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef60`](#insn-00afef60)

~~~json
{
  "source": "00afef60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef64`](#insn-00afef64)

~~~json
{
  "source": "00afef64",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef68`](#insn-00afef68)

~~~json
{
  "source": "00afef68",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef6c`](#insn-00afef6c)

~~~json
{
  "source": "00afef6c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef70`](#insn-00afef70)

~~~json
{
  "source": "00afef70",
  "target": "00b04854",
  "target_space": "ram",
  "resolution": "function"
}
~~~
