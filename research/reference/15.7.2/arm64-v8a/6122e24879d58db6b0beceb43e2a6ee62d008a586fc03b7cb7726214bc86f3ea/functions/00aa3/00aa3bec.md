# 00aa3bec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aa3bec`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3bec.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0007.md#compare-c952c065be93f793004dfbbaea5e4a3d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa3bec",
  "name": "FUN_00aa3bec",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "43761f6a4946da0ebfde6d4af26b359447d5dc2575e28ac02a86340a84d34a1a",
  "source_text_sha256": "43761f6a4946da0ebfde6d4af26b359447d5dc2575e28ac02a86340a84d34a1a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa3bec",
        "00aa3cab"
      ]
    ],
    "bytes_sha256": "1ea1fe142f2012fdf48dc28e23e10da4d102848bf4540e5b4deb76e572f360fe",
    "instruction_count": 48,
    "instruction_bytes": 192,
    "body_bytes": 192,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0065f258](../0065f/0065f258.md)
- [0069ef54](../0069e/0069ef54.md)
- [009f1e64](../009f1/009f1e64.md)
- [00a960ac](../00a96/00a960ac.md)
- [00aa0f20](../00aa0/00aa0f20.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)
- [00aa4fb0](../00aa4/00aa4fb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1142 bytes

~~~c

ulong FUN_00aa3bec(int param_1,int param_2,int param_3,ulong param_4)

{
  int iVar1;
  long lVar2;
  ulong uVar3;
  
                    /* try { // try from 00aa3c04 to 00ba3c13 has its CatchHandler @ 00aa599c */
  lVar2 = FUN_0081f580();
                    /* try { // try from 00aa3c14 to 00ba3c27 has its CatchHandler @ 00aa5974 */
  uVar3 = FUN_005c2710(lVar2 + (long)param_1 * 0x1f0 + 0x2678);
                    /* try { // try from 00aa3c28 to 00ba3c5f has its CatchHandler @ 00aa3a30 */
  lVar2 = FUN_0081f580();
  if ((uVar3 & 1) == 0) {
    uVar3 = (ulong)(*(int *)((long)__DT_JMPREL + lVar2 + ((long)param_2 + 2) * 0x1c4 + 0xa4e4) != 0)
    ;
  }
  else {
                    /* try { // try from 00aa3c74 to 00ba3c87 has its CatchHandler @ 00aa59e0 */
    iVar1 = *(int *)(lVar2 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f008);
    uVar3 = (ulong)(iVar1 != 0);
    if ((iVar1 == 0) && ((param_4 & 1) != 0)) {
      uVar3 = FUN_00aa4fb0(0,param_2,param_3,0x800);
      return uVar3;
    }
  }
                    /* try { // try from 00aa3c60 to 00ba3c73 has its CatchHandler @ 00aa59e4 */
  return uVar3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aa3bec"></a> `00aa3bec` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aa3bf0"></a> `00aa3bf0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa3bf4"></a> `00aa3bf4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa3bf8"></a> `00aa3bf8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aa3bfc"></a> `00aa3bfc` | `f5 03 03 2a` | mov w21,w3 | `FALL_THROUGH`
<a id="insn-00aa3c00"></a> `00aa3c00` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00aa3c04"></a> `00aa3c04` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00aa3c08"></a> `00aa3c08` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00aa3c0c"></a> `00aa3c0c` | `5d ee f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa3c10"></a> `00aa3c10` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00aa3c14"></a> `00aa3c14` | `09 cf 84 52` | mov w9,#0x2678 | `FALL_THROUGH`
<a id="insn-00aa3c18"></a> `00aa3c18` | `c8 02 28 9b` | smaddl x8,w22,w8,x0 | `FALL_THROUGH`
<a id="insn-00aa3c1c"></a> `00aa3c1c` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00aa3c20"></a> `00aa3c20` | `bc 7a ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00aa3c24"></a> `00aa3c24` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00aa3c28"></a> `00aa3c28` | `56 ee f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa3c2c"></a> `00aa3c2c` | `88 7e 40 93` | sxtw x8,w20 | `FALL_THROUGH`
<a id="insn-00aa3c30"></a> `00aa3c30` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00aa3c34"></a> `00aa3c34` | `96 01 00 37` | tbnz w22,#0x0,0x00aa3c64 | `CONDITIONAL_JUMP`
<a id="insn-00aa3c38"></a> `00aa3c38` | `89 38 80 52` | mov w9,#0x1c4 | `FALL_THROUGH`
<a id="insn-00aa3c3c"></a> `00aa3c3c` | `08 01 09 9b` | madd x8,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00aa3c40"></a> `00aa3c40` | `89 e3 93 52` | mov w9,#0x9f1c | `FALL_THROUGH`
<a id="insn-00aa3c44"></a> `00aa3c44` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa3c48"></a> `00aa3c48` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa3c4c"></a> `00aa3c4c` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00aa3c50"></a> `00aa3c50` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00aa3c54"></a> `00aa3c54` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa3c58"></a> `00aa3c58` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa3c5c"></a> `00aa3c5c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aa3c60"></a> `00aa3c60` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aa3c64"></a> `00aa3c64` | `09 ee 80 52` | mov w9,#0x770 | `FALL_THROUGH`
<a id="insn-00aa3c68"></a> `00aa3c68` | `08 01 09 9b` | madd x8,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00aa3c6c"></a> `00aa3c6c` | `89 3b 80 52` | mov w9,#0x1dc | `FALL_THROUGH`
<a id="insn-00aa3c70"></a> `00aa3c70` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00aa3c74"></a> `00aa3c74` | `09 01 9e 52` | mov w9,#0xf008 | `FALL_THROUGH`
<a id="insn-00aa3c78"></a> `00aa3c78` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa3c7c"></a> `00aa3c7c` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa3c80"></a> `00aa3c80` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00aa3c84"></a> `00aa3c84` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00aa3c88"></a> `00aa3c88` | `68 fe ff 35` | cbnz w8,0x00aa3c54 | `CONDITIONAL_JUMP`
<a id="insn-00aa3c8c"></a> `00aa3c8c` | `55 fe 07 36` | tbz w21,#0x0,0x00aa3c54 | `CONDITIONAL_JUMP`
<a id="insn-00aa3c90"></a> `00aa3c90` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00aa3c94"></a> `00aa3c94` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00aa3c98"></a> `00aa3c98` | `03 00 81 52` | mov w3,#0x800 | `FALL_THROUGH`
<a id="insn-00aa3c9c"></a> `00aa3c9c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa3ca0"></a> `00aa3ca0` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa3ca4"></a> `00aa3ca4` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aa3ca8"></a> `00aa3ca8` | `c2 04 00 14` | b 0x00aa4fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa3bec`](#insn-00aa3bec) 範囲 `[['00aa3bec', '00aa3c03']]`
  - `FALL_THROUGH` [`00aa3c00`](#insn-00aa3c00) → [`00aa3c04`](#insn-00aa3c04)
- ブロック [`00aa3c04`](#insn-00aa3c04) 範囲 `[['00aa3c04', '00aa3c13']]`
  - `FALL_THROUGH` [`00aa3c10`](#insn-00aa3c10) → [`00aa3c14`](#insn-00aa3c14)
- ブロック [`00aa3c14`](#insn-00aa3c14) 範囲 `[['00aa3c14', '00aa3c27']]`
  - `FALL_THROUGH` [`00aa3c24`](#insn-00aa3c24) → [`00aa3c28`](#insn-00aa3c28)
- ブロック [`00aa3c28`](#insn-00aa3c28) 範囲 `[['00aa3c28', '00aa3c37']]`
  - `CONDITIONAL_JUMP` [`00aa3c34`](#insn-00aa3c34) → [`00aa3c64`](#insn-00aa3c64)
  - `FALL_THROUGH` [`00aa3c34`](#insn-00aa3c34) → [`00aa3c38`](#insn-00aa3c38)
- ブロック [`00aa3c38`](#insn-00aa3c38) 範囲 `[['00aa3c38', '00aa3c53']]`
  - `FALL_THROUGH` [`00aa3c50`](#insn-00aa3c50) → [`00aa3c54`](#insn-00aa3c54)
- ブロック [`00aa3c54`](#insn-00aa3c54) 範囲 `[['00aa3c54', '00aa3c5f']]`
  - `FALL_THROUGH` [`00aa3c5c`](#insn-00aa3c5c) → [`00aa3c60`](#insn-00aa3c60)
- ブロック [`00aa3c60`](#insn-00aa3c60) 範囲 `[['00aa3c60', '00aa3c63']]`
- ブロック [`00aa3c64`](#insn-00aa3c64) 範囲 `[['00aa3c64', '00aa3c73']]`
  - `FALL_THROUGH` [`00aa3c70`](#insn-00aa3c70) → [`00aa3c74`](#insn-00aa3c74)
- ブロック [`00aa3c74`](#insn-00aa3c74) 範囲 `[['00aa3c74', '00aa3c8b']]`
  - `CONDITIONAL_JUMP` [`00aa3c88`](#insn-00aa3c88) → [`00aa3c54`](#insn-00aa3c54)
  - `FALL_THROUGH` [`00aa3c88`](#insn-00aa3c88) → [`00aa3c8c`](#insn-00aa3c8c)
- ブロック [`00aa3c8c`](#insn-00aa3c8c) 範囲 `[['00aa3c8c', '00aa3c8f']]`
  - `CONDITIONAL_JUMP` [`00aa3c8c`](#insn-00aa3c8c) → [`00aa3c54`](#insn-00aa3c54)
  - `FALL_THROUGH` [`00aa3c8c`](#insn-00aa3c8c) → [`00aa3c90`](#insn-00aa3c90)
- ブロック [`00aa3c90`](#insn-00aa3c90) 範囲 `[['00aa3c90', '00aa3cab']]`

## 命令位置別の参照

- [`00aa3bec`](#insn-00aa3bec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3bf0`](#insn-00aa3bf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3bf4`](#insn-00aa3bf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3c0c`](#insn-00aa3c0c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa3c20`](#insn-00aa3c20) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00aa3c28`](#insn-00aa3c28) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa3c34`](#insn-00aa3c34) → [`00aa3c64`](#insn-00aa3c64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3c48`](#insn-00aa3c48) → `00239f1c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1792]`
- [`00aa3c54`](#insn-00aa3c54) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3c58`](#insn-00aa3c58) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3c5c`](#insn-00aa3c5c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3c88`](#insn-00aa3c88) → [`00aa3c54`](#insn-00aa3c54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3c8c`](#insn-00aa3c8c) → [`00aa3c54`](#insn-00aa3c54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3c9c`](#insn-00aa3c9c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3ca0`](#insn-00aa3ca0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3ca4`](#insn-00aa3ca4) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3ca8`](#insn-00aa3ca8) → [`00aa4fb0`](../00aa4/00aa4fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aa4fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa3bec`](#insn-00aa3bec)

~~~json
{
  "source": "00aa3bec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3bf0`](#insn-00aa3bf0)

~~~json
{
  "source": "00aa3bf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3bf4`](#insn-00aa3bf4)

~~~json
{
  "source": "00aa3bf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3c0c`](#insn-00aa3c0c)

~~~json
{
  "source": "00aa3c0c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa3c20`](#insn-00aa3c20)

~~~json
{
  "source": "00aa3c20",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa3c28`](#insn-00aa3c28)

~~~json
{
  "source": "00aa3c28",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa3c34`](#insn-00aa3c34)

~~~json
{
  "source": "00aa3c34",
  "target": "00aa3c64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3c48`](#insn-00aa3c48)

~~~json
{
  "source": "00aa3c48",
  "target": "00239f1c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0022fa38",
  "offset": 42212,
  "size": 43008,
  "datatype": "Elf64_Rela[1792]",
  "bytes": "a0bfb1000000000002040000010000000000000000000000a8bfb10000000000",
  "capture_start": "0022fa38",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aa3c54`](#insn-00aa3c54)

~~~json
{
  "source": "00aa3c54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3c58`](#insn-00aa3c58)

~~~json
{
  "source": "00aa3c58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3c5c`](#insn-00aa3c5c)

~~~json
{
  "source": "00aa3c5c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3c88`](#insn-00aa3c88)

~~~json
{
  "source": "00aa3c88",
  "target": "00aa3c54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3c8c`](#insn-00aa3c8c)

~~~json
{
  "source": "00aa3c8c",
  "target": "00aa3c54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3c9c`](#insn-00aa3c9c)

~~~json
{
  "source": "00aa3c9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3ca0`](#insn-00aa3ca0)

~~~json
{
  "source": "00aa3ca0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3ca4`](#insn-00aa3ca4)

~~~json
{
  "source": "00aa3ca4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3ca8`](#insn-00aa3ca8)

~~~json
{
  "source": "00aa3ca8",
  "target": "00aa4fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
