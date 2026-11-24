# 00a7dadc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0159.md#review-2fa0e6438daddeaf045000b923b29841)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0040.md#review-2fa0e6438daddeaf045000b923b29841)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a7dadc",
  "name": "FUN_00a7dadc",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "65461ea07e741e807c37964e7f2b3f7b3816b099bf39b944c73e71dd9fa937bb",
  "source_text_sha256": "65461ea07e741e807c37964e7f2b3f7b3816b099bf39b944c73e71dd9fa937bb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a7dadc",
        "00a7db9b"
      ]
    ],
    "bytes_sha256": "212e42e7ee210a830e96eace6be52a25c2f2b77038434e7a64a5ba79f13d8c01",
    "instruction_count": 48,
    "instruction_bytes": 192,
    "body_bytes": 192,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00b3dfe8](../00b3d/00b3dfe8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 843 bytes

~~~c

void FUN_00a7dadc(long param_1)

{
  ulong uVar1;
  long lVar2;
  
  lVar2 = *(long *)(param_1 + 8);
  *(undefined4 *)((long)&fde_table_entry_0033e2e0.initial_loc + lVar2) = 0;
  if ((((*(byte *)((long)&DWORD_0042ef40 + lVar2) & 1) == 0) &&
      (*(int *)(&uleb128_0042ef44 + lVar2) == 0)) &&
     (uVar1 = FUN_00b3dfe8(lVar2 + 0x2350,0x47), (uVar1 & 1) != 0)) {
    *(undefined4 *)((long)&QWORD_0039b1b4 + lVar2) = 2;
    *(byte *)((long)&DWORD_0042ef40 + lVar2) = 1;
    *(undefined4 *)(lVar2 + 0x3478) = 0x1c;
  }
  if ((((*(byte *)(lVar2 + 0x16f0) & 1) == 0) && (*(int *)(&uleb128_0042ef44 + lVar2) == 2)) &&
     (uVar1 = FUN_00b3dfe8(lVar2 + 0x2350,0x47), (uVar1 & 1) != 0)) {
    *(undefined1 *)(lVar2 + 0x16f0) = 1;
    *(undefined4 *)((long)&QWORD_0039b1b4 + lVar2) = 2;
    *(undefined4 *)(lVar2 + 0x3478) = 0x26;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a7dadc"></a> `00a7dadc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00a7dae0"></a> `00a7dae0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a7dae4"></a> `00a7dae4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a7dae8"></a> `00a7dae8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a7daec"></a> `00a7daec` | `13 04 40 f9` | ldr x19,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00a7daf0"></a> `00a7daf0` | `09 5c 9c 52` | mov w9,#0xe2e0 | `FALL_THROUGH`
<a id="insn-00a7daf4"></a> `00a7daf4` | `94 36 96 52` | mov w20,#0xb1b4 | `FALL_THROUGH`
<a id="insn-00a7daf8"></a> `00a7daf8` | `69 06 a0 72` | movk w9,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00a7dafc"></a> `00a7dafc` | `34 07 a0 72` | movk w20,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00a7db00"></a> `00a7db00` | `15 de 82 52` | mov w21,#0x16f0 | `FALL_THROUGH`
<a id="insn-00a7db04"></a> `00a7db04` | `68 ba 50 91` | add x8,x19,#0x42e, LSL #12 | `FALL_THROUGH`
<a id="insn-00a7db08"></a> `00a7db08` | `7f 6a 29 b8` | str wzr,[x19, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a7db0c"></a> `00a7db0c` | `16 01 3d 91` | add x22,x8,#0xf40 | `FALL_THROUGH`
<a id="insn-00a7db10"></a> `00a7db10` | `c8 02 40 39` | ldrb w8,[x22] | `FALL_THROUGH`
<a id="insn-00a7db14"></a> `00a7db14` | `c8 01 00 37` | tbnz w8,#0x0,0x00a7db4c | `CONDITIONAL_JUMP`
<a id="insn-00a7db18"></a> `00a7db18` | `c8 06 40 b9` | ldr w8,[x22, #0x4] | `FALL_THROUGH`
<a id="insn-00a7db1c"></a> `00a7db1c` | `88 01 00 35` | cbnz w8,0x00a7db4c | `CONDITIONAL_JUMP`
<a id="insn-00a7db20"></a> `00a7db20` | `08 6a 84 52` | mov w8,#0x2350 | `FALL_THROUGH`
<a id="insn-00a7db24"></a> `00a7db24` | `e1 08 80 52` | mov w1,#0x47 | `FALL_THROUGH`
<a id="insn-00a7db28"></a> `00a7db28` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00a7db2c"></a> `00a7db2c` | `2f 01 03 94` | bl 0x00b3dfe8 | `UNCONDITIONAL_CALL`
<a id="insn-00a7db30"></a> `00a7db30` | `e0 00 00 36` | tbz w0,#0x0,0x00a7db4c | `CONDITIONAL_JUMP`
<a id="insn-00a7db34"></a> `00a7db34` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00a7db38"></a> `00a7db38` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00a7db3c"></a> `00a7db3c` | `69 6a 34 b8` | str w9,[x19, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a7db40"></a> `00a7db40` | `89 03 80 52` | mov w9,#0x1c | `FALL_THROUGH`
<a id="insn-00a7db44"></a> `00a7db44` | `c8 02 00 39` | strb w8,[x22] | `FALL_THROUGH`
<a id="insn-00a7db48"></a> `00a7db48` | `69 7a 34 b9` | str w9,[x19, #0x3478] | `FALL_THROUGH`
<a id="insn-00a7db4c"></a> `00a7db4c` | `68 6a 75 38` | ldrb w8,[x19, x21, LSL ] | `FALL_THROUGH`
<a id="insn-00a7db50"></a> `00a7db50` | `e8 01 00 37` | tbnz w8,#0x0,0x00a7db8c | `CONDITIONAL_JUMP`
<a id="insn-00a7db54"></a> `00a7db54` | `c8 06 40 b9` | ldr w8,[x22, #0x4] | `FALL_THROUGH`
<a id="insn-00a7db58"></a> `00a7db58` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00a7db5c"></a> `00a7db5c` | `81 01 00 54` | b.ne 0x00a7db8c | `CONDITIONAL_JUMP`
<a id="insn-00a7db60"></a> `00a7db60` | `08 6a 84 52` | mov w8,#0x2350 | `FALL_THROUGH`
<a id="insn-00a7db64"></a> `00a7db64` | `e1 08 80 52` | mov w1,#0x47 | `FALL_THROUGH`
<a id="insn-00a7db68"></a> `00a7db68` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00a7db6c"></a> `00a7db6c` | `1f 01 03 94` | bl 0x00b3dfe8 | `UNCONDITIONAL_CALL`
<a id="insn-00a7db70"></a> `00a7db70` | `e0 00 00 36` | tbz w0,#0x0,0x00a7db8c | `CONDITIONAL_JUMP`
<a id="insn-00a7db74"></a> `00a7db74` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00a7db78"></a> `00a7db78` | `68 6a 35 38` | strb w8,[x19, x21, LSL ] | `FALL_THROUGH`
<a id="insn-00a7db7c"></a> `00a7db7c` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-00a7db80"></a> `00a7db80` | `68 6a 34 b8` | str w8,[x19, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a7db84"></a> `00a7db84` | `c8 04 80 52` | mov w8,#0x26 | `FALL_THROUGH`
<a id="insn-00a7db88"></a> `00a7db88` | `68 7a 34 b9` | str w8,[x19, #0x3478] | `FALL_THROUGH`
<a id="insn-00a7db8c"></a> `00a7db8c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a7db90"></a> `00a7db90` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a7db94"></a> `00a7db94` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00a7db98"></a> `00a7db98` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a7dadc`](#insn-00a7dadc) 範囲 `[['00a7dadc', '00a7db17']]`
  - `CONDITIONAL_JUMP` [`00a7db14`](#insn-00a7db14) → [`00a7db4c`](#insn-00a7db4c)
  - `FALL_THROUGH` [`00a7db14`](#insn-00a7db14) → [`00a7db18`](#insn-00a7db18)
- ブロック [`00a7db18`](#insn-00a7db18) 範囲 `[['00a7db18', '00a7db1f']]`
  - `CONDITIONAL_JUMP` [`00a7db1c`](#insn-00a7db1c) → [`00a7db4c`](#insn-00a7db4c)
  - `FALL_THROUGH` [`00a7db1c`](#insn-00a7db1c) → [`00a7db20`](#insn-00a7db20)
- ブロック [`00a7db20`](#insn-00a7db20) 範囲 `[['00a7db20', '00a7db33']]`
  - `CONDITIONAL_JUMP` [`00a7db30`](#insn-00a7db30) → [`00a7db4c`](#insn-00a7db4c)
  - `FALL_THROUGH` [`00a7db30`](#insn-00a7db30) → [`00a7db34`](#insn-00a7db34)
- ブロック [`00a7db34`](#insn-00a7db34) 範囲 `[['00a7db34', '00a7db4b']]`
  - `FALL_THROUGH` [`00a7db48`](#insn-00a7db48) → [`00a7db4c`](#insn-00a7db4c)
- ブロック [`00a7db4c`](#insn-00a7db4c) 範囲 `[['00a7db4c', '00a7db53']]`
  - `CONDITIONAL_JUMP` [`00a7db50`](#insn-00a7db50) → [`00a7db8c`](#insn-00a7db8c)
  - `FALL_THROUGH` [`00a7db50`](#insn-00a7db50) → [`00a7db54`](#insn-00a7db54)
- ブロック [`00a7db54`](#insn-00a7db54) 範囲 `[['00a7db54', '00a7db5f']]`
  - `CONDITIONAL_JUMP` [`00a7db5c`](#insn-00a7db5c) → [`00a7db8c`](#insn-00a7db8c)
  - `FALL_THROUGH` [`00a7db5c`](#insn-00a7db5c) → [`00a7db60`](#insn-00a7db60)
- ブロック [`00a7db60`](#insn-00a7db60) 範囲 `[['00a7db60', '00a7db73']]`
  - `CONDITIONAL_JUMP` [`00a7db70`](#insn-00a7db70) → [`00a7db8c`](#insn-00a7db8c)
  - `FALL_THROUGH` [`00a7db70`](#insn-00a7db70) → [`00a7db74`](#insn-00a7db74)
- ブロック [`00a7db74`](#insn-00a7db74) 範囲 `[['00a7db74', '00a7db8b']]`
  - `FALL_THROUGH` [`00a7db88`](#insn-00a7db88) → [`00a7db8c`](#insn-00a7db8c)
- ブロック [`00a7db8c`](#insn-00a7db8c) 範囲 `[['00a7db8c', '00a7db9b']]`

## 命令位置別の参照

- [`00a7dadc`](#insn-00a7dadc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dae0`](#insn-00a7dae0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dae4`](#insn-00a7dae4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7db08`](#insn-00a7db08) → `0033e2e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a7db10`](#insn-00a7db10) → `0042ef40`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00a7db14`](#insn-00a7db14) → [`00a7db4c`](#insn-00a7db4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7db18`](#insn-00a7db18) → `0042ef44`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00a7db1c`](#insn-00a7db1c) → [`00a7db4c`](#insn-00a7db4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7db2c`](#insn-00a7db2c) → [`00b3dfe8`](../00b3d/00b3dfe8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b3dfe8` · 推定シンボル `None` · 推定型 `None`
- [`00a7db30`](#insn-00a7db30) → [`00a7db4c`](#insn-00a7db4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7db3c`](#insn-00a7db3c) → `0039b1b4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00a7db44`](#insn-00a7db44) → `0042ef40`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00a7db50`](#insn-00a7db50) → [`00a7db8c`](#insn-00a7db8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7db54`](#insn-00a7db54) → `0042ef44`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00a7db5c`](#insn-00a7db5c) → [`00a7db8c`](#insn-00a7db8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7db6c`](#insn-00a7db6c) → [`00b3dfe8`](../00b3d/00b3dfe8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b3dfe8` · 推定シンボル `None` · 推定型 `None`
- [`00a7db70`](#insn-00a7db70) → [`00a7db8c`](#insn-00a7db8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7db80`](#insn-00a7db80) → `0039b1b4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00a7db8c`](#insn-00a7db8c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7db90`](#insn-00a7db90) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7db94`](#insn-00a7db94) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a7dadc`](#insn-00a7dadc)

~~~json
{
  "source": "00a7dadc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dae0`](#insn-00a7dae0)

~~~json
{
  "source": "00a7dae0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dae4`](#insn-00a7dae4)

~~~json
{
  "source": "00a7dae4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7db08`](#insn-00a7db08)

~~~json
{
  "source": "00a7db08",
  "target": "0033e2e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033e2e0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "5c5f8b0004060c00",
  "capture_start": "0033e2e0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a7db10`](#insn-00a7db10)

~~~json
{
  "source": "00a7db10",
  "target": "0042ef40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0042ef40",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "38010000",
  "capture_start": "0042ef40",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a7db14`](#insn-00a7db14)

~~~json
{
  "source": "00a7db14",
  "target": "00a7db4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7db18`](#insn-00a7db18)

~~~json
{
  "source": "00a7db18",
  "target": "0042ef44",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0042ef44",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "08",
  "capture_start": "0042ef44",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a7db1c`](#insn-00a7db1c)

~~~json
{
  "source": "00a7db1c",
  "target": "00a7db4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7db2c`](#insn-00a7db2c)

~~~json
{
  "source": "00a7db2c",
  "target": "00b3dfe8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7db30`](#insn-00a7db30)

~~~json
{
  "source": "00a7db30",
  "target": "00a7db4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7db3c`](#insn-00a7db3c)

~~~json
{
  "source": "00a7db3c",
  "target": "0039b1b4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b1b4",
  "offset": 0,
  "size": 8,
  "datatype": "qword",
  "bytes": "0c00000000000000",
  "capture_start": "0039b1b4",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a7db44`](#insn-00a7db44)

~~~json
{
  "source": "00a7db44",
  "target": "0042ef40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0042ef40",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "38010000",
  "capture_start": "0042ef40",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a7db50`](#insn-00a7db50)

~~~json
{
  "source": "00a7db50",
  "target": "00a7db8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7db54`](#insn-00a7db54)

~~~json
{
  "source": "00a7db54",
  "target": "0042ef44",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0042ef44",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "08",
  "capture_start": "0042ef44",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a7db5c`](#insn-00a7db5c)

~~~json
{
  "source": "00a7db5c",
  "target": "00a7db8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7db6c`](#insn-00a7db6c)

~~~json
{
  "source": "00a7db6c",
  "target": "00b3dfe8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7db70`](#insn-00a7db70)

~~~json
{
  "source": "00a7db70",
  "target": "00a7db8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7db80`](#insn-00a7db80)

~~~json
{
  "source": "00a7db80",
  "target": "0039b1b4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b1b4",
  "offset": 0,
  "size": 8,
  "datatype": "qword",
  "bytes": "0c00000000000000",
  "capture_start": "0039b1b4",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a7db8c`](#insn-00a7db8c)

~~~json
{
  "source": "00a7db8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7db90`](#insn-00a7db90)

~~~json
{
  "source": "00a7db90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7db94`](#insn-00a7db94)

~~~json
{
  "source": "00a7db94",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
