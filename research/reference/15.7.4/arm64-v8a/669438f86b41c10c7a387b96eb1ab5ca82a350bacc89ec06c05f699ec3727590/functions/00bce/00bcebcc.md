# 00bcebcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bceb88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bceb88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-1ff5be6ad86b3f632dcbfc05ce9ef7dc)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c4b614`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b614.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0021.md#compare-20bf602c7217fe67d1a57253db640410)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcebcc",
  "name": "FUN_00bcebcc",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1535a6e4d4024a9e6134669794e5f4e19dd46d4a9e316bd866b7df9321eab096",
  "source_text_sha256": "1535a6e4d4024a9e6134669794e5f4e19dd46d4a9e316bd866b7df9321eab096",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcebcc",
        "00bceccf"
      ]
    ],
    "bytes_sha256": "c9083ec4faf390b5a2d165023bff631f82c717eb0d3a871aa783098f0928a85b",
    "instruction_count": 65,
    "instruction_bytes": 260,
    "body_bytes": 260,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1256 bytes

~~~c

void FUN_00bcebcc(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  void *__ptr;
  long lVar2;
  size_t __size;
  long *plVar3;
  
  plVar3 = *(long **)(param_1 + 0x10);
  (**(code **)(*plVar3 + 0x20))(plVar3);
  if ((*(ushort *)((long)plVar3 + 9) & 0xc0) != 0x40) {
    (**(code **)(*plVar3 + 0x28))(plVar3,param_2);
  }
  lVar2 = param_2[1];
  __ptr = (void *)*param_2;
  if ((ulong)param_2[2] < lVar2 + 2U) {
    __size = param_2[2] * 2;
    uVar1 = lVar2 + 0x3e2;
    if (__size < uVar1 || __size - uVar1 == 0) {
      __size = uVar1;
    }
    param_2[2] = __size;
    __ptr = realloc(__ptr,__size);
    *param_2 = __ptr;
    if (__ptr == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
  }
  *(undefined2 *)((long)__ptr + lVar2) = 0x3a3a;
  plVar3 = *(long **)(param_1 + 0x18);
  lVar2 = *plVar3;
  param_2[1] = param_2[1] + 2;
  (**(code **)(lVar2 + 0x20))(plVar3,param_2);
  if ((*(ushort *)((long)plVar3 + 9) & 0xc0) == 0x40) {
    return;
  }
                    /* WARNING: Could not recover jumptable at 0x00bcecc8. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar3 + 0x28))(plVar3,param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcebcc"></a> `00bcebcc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcebd0"></a> `00bcebd0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcebd4"></a> `00bcebd4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcebd8"></a> `00bcebd8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcebdc"></a> `00bcebdc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcebe0"></a> `00bcebe0` | `15 08 40 f9` | ldr x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bcebe4"></a> `00bcebe4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcebe8"></a> `00bcebe8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcebec"></a> `00bcebec` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcebf0"></a> `00bcebf0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcebf4"></a> `00bcebf4` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bcebf8"></a> `00bcebf8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcebfc"></a> `00bcebfc` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bcec00"></a> `00bcec00` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcec04"></a> `00bcec04` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bcec08"></a> `00bcec08` | `c0 00 00 54` | b.eq 0x00bcec20 | `CONDITIONAL_JUMP`
<a id="insn-00bcec0c"></a> `00bcec0c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcec10"></a> `00bcec10` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcec14"></a> `00bcec14` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcec18"></a> `00bcec18` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bcec1c"></a> `00bcec1c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcec20"></a> `00bcec20` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcec24"></a> `00bcec24` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcec28"></a> `00bcec28` | `0a 09 00 91` | add x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bcec2c"></a> `00bcec2c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcec30"></a> `00bcec30` | `49 01 00 54` | b.ls 0x00bcec58 | `CONDITIONAL_JUMP`
<a id="insn-00bcec34"></a> `00bcec34` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcec38"></a> `00bcec38` | `08 89 0f 91` | add x8,x8,#0x3e2 | `FALL_THROUGH`
<a id="insn-00bcec3c"></a> `00bcec3c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcec40"></a> `00bcec40` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcec44"></a> `00bcec44` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcec48"></a> `00bcec48` | `82 39 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bcec4c"></a> `00bcec4c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcec50"></a> `00bcec50` | `e0 03 00 b4` | cbz x0,0x00bceccc | `CONDITIONAL_JUMP`
<a id="insn-00bcec54"></a> `00bcec54` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcec58"></a> `00bcec58` | `49 47 87 52` | mov w9,#0x3a3a | `FALL_THROUGH`
<a id="insn-00bcec5c"></a> `00bcec5c` | `09 68 28 78` | strh w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bcec60"></a> `00bcec60` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcec64"></a> `00bcec64` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcec68"></a> `00bcec68` | `94 0e 40 f9` | ldr x20,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bcec6c"></a> `00bcec6c` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bcec70"></a> `00bcec70` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00bcec74"></a> `00bcec74` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcec78"></a> `00bcec78` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcec7c"></a> `00bcec7c` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bcec80"></a> `00bcec80` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcec84"></a> `00bcec84` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bcec88"></a> `00bcec88` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcec8c"></a> `00bcec8c` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bcec90"></a> `00bcec90` | `c1 00 00 54` | b.ne 0x00bceca8 | `CONDITIONAL_JUMP`
<a id="insn-00bcec94"></a> `00bcec94` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcec98"></a> `00bcec98` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcec9c"></a> `00bcec9c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bceca0"></a> `00bceca0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bceca4"></a> `00bceca4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bceca8"></a> `00bceca8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcecac"></a> `00bcecac` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcecb0"></a> `00bcecb0` | `10 15 40 f9` | ldr x16,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bcecb4"></a> `00bcecb4` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcecb8"></a> `00bcecb8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcecbc"></a> `00bcecbc` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcecc0"></a> `00bcecc0` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcecc4"></a> `00bcecc4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcecc8"></a> `00bcecc8` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00bceccc"></a> `00bceccc` | `7d 3d 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcebcc`](#insn-00bcebcc) 範囲 `[['00bcebcc', '00bcec0b']]`
  - `CONDITIONAL_JUMP` [`00bcec08`](#insn-00bcec08) → [`00bcec20`](#insn-00bcec20)
  - `FALL_THROUGH` [`00bcec08`](#insn-00bcec08) → [`00bcec0c`](#insn-00bcec0c)
- ブロック [`00bcec0c`](#insn-00bcec0c) 範囲 `[['00bcec0c', '00bcec1f']]`
  - `FALL_THROUGH` [`00bcec1c`](#insn-00bcec1c) → [`00bcec20`](#insn-00bcec20)
- ブロック [`00bcec20`](#insn-00bcec20) 範囲 `[['00bcec20', '00bcec33']]`
  - `CONDITIONAL_JUMP` [`00bcec30`](#insn-00bcec30) → [`00bcec58`](#insn-00bcec58)
  - `FALL_THROUGH` [`00bcec30`](#insn-00bcec30) → [`00bcec34`](#insn-00bcec34)
- ブロック [`00bcec34`](#insn-00bcec34) 範囲 `[['00bcec34', '00bcec53']]`
  - `CONDITIONAL_JUMP` [`00bcec50`](#insn-00bcec50) → [`00bceccc`](#insn-00bceccc)
  - `FALL_THROUGH` [`00bcec50`](#insn-00bcec50) → [`00bcec54`](#insn-00bcec54)
- ブロック [`00bcec54`](#insn-00bcec54) 範囲 `[['00bcec54', '00bcec57']]`
  - `FALL_THROUGH` [`00bcec54`](#insn-00bcec54) → [`00bcec58`](#insn-00bcec58)
- ブロック [`00bcec58`](#insn-00bcec58) 範囲 `[['00bcec58', '00bcec93']]`
  - `CONDITIONAL_JUMP` [`00bcec90`](#insn-00bcec90) → [`00bceca8`](#insn-00bceca8)
  - `FALL_THROUGH` [`00bcec90`](#insn-00bcec90) → [`00bcec94`](#insn-00bcec94)
- ブロック [`00bcec94`](#insn-00bcec94) 範囲 `[['00bcec94', '00bceca7']]`
- ブロック [`00bceca8`](#insn-00bceca8) 範囲 `[['00bceca8', '00bceccb']]`
- ブロック [`00bceccc`](#insn-00bceccc) 範囲 `[['00bceccc', '00bceccf']]`

## 命令位置別の参照

- [`00bcebd0`](#insn-00bcebd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcebd4`](#insn-00bcebd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcebd8`](#insn-00bcebd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec08`](#insn-00bcec08) → [`00bcec20`](#insn-00bcec20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec30`](#insn-00bcec30) → [`00bcec58`](#insn-00bcec58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec48`](#insn-00bcec48) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bcec50`](#insn-00bcec50) → [`00bceccc`](#insn-00bceccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec90`](#insn-00bcec90) → [`00bceca8`](#insn-00bceca8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec94`](#insn-00bcec94) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec98`](#insn-00bcec98) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec9c`](#insn-00bcec9c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecb8`](#insn-00bcecb8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecbc`](#insn-00bcecbc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecc0`](#insn-00bcecc0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceccc`](#insn-00bceccc) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcebd0`](#insn-00bcebd0)

~~~json
{
  "source": "00bcebd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcebd4`](#insn-00bcebd4)

~~~json
{
  "source": "00bcebd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcebd8`](#insn-00bcebd8)

~~~json
{
  "source": "00bcebd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec08`](#insn-00bcec08)

~~~json
{
  "source": "00bcec08",
  "target": "00bcec20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec30`](#insn-00bcec30)

~~~json
{
  "source": "00bcec30",
  "target": "00bcec58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec48`](#insn-00bcec48)

~~~json
{
  "source": "00bcec48",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcec50`](#insn-00bcec50)

~~~json
{
  "source": "00bcec50",
  "target": "00bceccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec90`](#insn-00bcec90)

~~~json
{
  "source": "00bcec90",
  "target": "00bceca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec94`](#insn-00bcec94)

~~~json
{
  "source": "00bcec94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec98`](#insn-00bcec98)

~~~json
{
  "source": "00bcec98",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec9c`](#insn-00bcec9c)

~~~json
{
  "source": "00bcec9c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecb8`](#insn-00bcecb8)

~~~json
{
  "source": "00bcecb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecbc`](#insn-00bcecbc)

~~~json
{
  "source": "00bcecbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecc0`](#insn-00bcecc0)

~~~json
{
  "source": "00bcecc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceccc`](#insn-00bceccc)

~~~json
{
  "source": "00bceccc",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
