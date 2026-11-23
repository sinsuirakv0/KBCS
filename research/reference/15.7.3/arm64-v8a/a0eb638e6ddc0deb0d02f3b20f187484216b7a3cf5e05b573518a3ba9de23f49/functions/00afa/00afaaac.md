# 00afaaac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00afa9e4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa9e4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-9dc5d9bed373140c166145adc5d668bf)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afaaf0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaaf0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-9702e620d9be57dd54ab8d4e0b8dae30)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afaaac",
  "name": "_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c906a5db1c4af231948b34723afa72e82bc52ea32b8da9a26d710f9c4c97a819",
  "source_text_sha256": "c906a5db1c4af231948b34723afa72e82bc52ea32b8da9a26d710f9c4c97a819",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afaaac",
        "00afab6b"
      ]
    ],
    "bytes_sha256": "405779696906f204c32205134af923d023ed8e6d9db8456db28c2287bad588a1",
    "instruction_count": 48,
    "instruction_bytes": 192,
    "body_bytes": 192,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde920](../00bde/00bde920.md)

## 呼び出し先

- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bde270](../00bde/00bde270.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1385 bytes

~~~c

void _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_
               (ulong *param_1,byte *param_2,ulong param_3,ulong param_4)

{
  ulong __n;
  byte bVar1;
  byte *pbVar2;
  void *__dest;
  ulong uVar3;
  
                    /* try { // try from 00afaab0 to 00bfaacf has its CatchHandler @ 00afff40 */
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  bVar1 = *param_2;
  uVar3 = (ulong)(bVar1 >> 1);
  if ((bVar1 & 1) != 0) {
    uVar3 = *(ulong *)(param_2 + 8);
  }
  if (uVar3 < param_3) {
LAB_00afab68:
                    /* WARNING: Subroutine does not return */
    abort();
  }
  pbVar2 = *(byte **)(param_2 + 0x10);
  if ((bVar1 & 1) == 0) {
    pbVar2 = param_2 + 1;
  }
  __n = uVar3 - param_3;
  if (param_4 <= uVar3 - param_3) {
    __n = param_4;
  }
  if (0xffffffffffffffef < __n) goto LAB_00afab68;
  if (__n < 0x17) {
    __dest = (void *)((long)param_1 + 1);
    *(char *)param_1 = (char)((int)__n << 1);
    if (__n == 0) goto LAB_00afab50;
  }
  else {
    uVar3 = __n + 0x10 & 0xfffffffffffffff0;
    __dest = (void *)_Znwm(uVar3);
    param_1[1] = __n;
    param_1[2] = (ulong)__dest;
    *param_1 = uVar3 | 1;
  }
                    /* try { // try from 00afab48 to 00bfab4f has its CatchHandler @ 00aff51c */
  memcpy(__dest,pbVar2 + param_3,__n);
LAB_00afab50:
  *(undefined1 *)((long)__dest + __n) = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afaaac"></a> `00afaaac` | `f7 0f 1c f8` | str x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00afaab0"></a> `00afaab0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaab4"></a> `00afaab4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afaab8"></a> `00afaab8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afaabc"></a> `00afaabc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00afaac0"></a> `00afaac0` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00afaac4"></a> `00afaac4` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00afaac8"></a> `00afaac8` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00afaacc"></a> `00afaacc` | `29 04 40 f9` | ldr x9,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00afaad0"></a> `00afaad0` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afaad4"></a> `00afaad4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afaad8"></a> `00afaad8` | `49 01 89 9a` | csel x9,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00afaadc"></a> `00afaadc` | `29 01 02 eb` | subs x9,x9,x2 | `FALL_THROUGH`
<a id="insn-00afaae0"></a> `00afaae0` | `43 04 00 54` | b.cc 0x00afab68 | `CONDITIONAL_JUMP`
<a id="insn-00afaae4"></a> `00afaae4` | `2a 08 40 f9` | ldr x10,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00afaae8"></a> `00afaae8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afaaec"></a> `00afaaec` | `57 15 81 9a` | csinc x23,x10,x1,ne | `FALL_THROUGH`
<a id="insn-00afaaf0"></a> `00afaaf0` | `3f 01 03 eb` | cmp x9,x3 | `FALL_THROUGH`
<a id="insn-00afaaf4"></a> `00afaaf4` | `35 31 83 9a` | csel x21,x9,x3,cc | `FALL_THROUGH`
<a id="insn-00afaaf8"></a> `00afaaf8` | `bf 42 00 b1` | cmn x21,#0x10 | `FALL_THROUGH`
<a id="insn-00afaafc"></a> `00afaafc` | `62 03 00 54` | b.cs 0x00afab68 | `CONDITIONAL_JUMP`
<a id="insn-00afab00"></a> `00afab00` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00afab04"></a> `00afab04` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afab08"></a> `00afab08` | `bf 5e 00 f1` | cmp x21,#0x17 | `FALL_THROUGH`
<a id="insn-00afab0c"></a> `00afab0c` | `a2 00 00 54` | b.cs 0x00afab20 | `CONDITIONAL_JUMP`
<a id="insn-00afab10"></a> `00afab10` | `a8 7a 1f 53` | lsl w8,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00afab14"></a> `00afab14` | `68 16 00 38` | strb w8,[x19], #0x1 | `FALL_THROUGH`
<a id="insn-00afab18"></a> `00afab18` | `55 01 00 b5` | cbnz x21,0x00afab40 | `CONDITIONAL_JUMP`
<a id="insn-00afab1c"></a> `00afab1c` | `0d 00 00 14` | b 0x00afab50 | `UNCONDITIONAL_JUMP`
<a id="insn-00afab20"></a> `00afab20` | `a8 42 00 91` | add x8,x21,#0x10 | `FALL_THROUGH`
<a id="insn-00afab24"></a> `00afab24` | `16 ed 7c 92` | and x22,x8,#-0x10 | `FALL_THROUGH`
<a id="insn-00afab28"></a> `00afab28` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00afab2c"></a> `00afab2c` | `31 81 03 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00afab30"></a> `00afab30` | `c8 02 40 b2` | orr x8,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00afab34"></a> `00afab34` | `75 82 00 a9` | stp x21,x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00afab38"></a> `00afab38` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00afab3c"></a> `00afab3c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afab40"></a> `00afab40` | `e1 02 14 8b` | add x1,x23,x20 | `FALL_THROUGH`
<a id="insn-00afab44"></a> `00afab44` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afab48"></a> `00afab48` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00afab4c"></a> `00afab4c` | `85 81 03 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00afab50"></a> `00afab50` | `7f 6a 35 38` | strb wzr,[x19, x21, LSL ] | `FALL_THROUGH`
<a id="insn-00afab54"></a> `00afab54` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afab58"></a> `00afab58` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afab5c"></a> `00afab5c` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afab60"></a> `00afab60` | `f7 07 44 f8` | ldr x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00afab64"></a> `00afab64` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afab68"></a> `00afab68` | `c2 8d 03 94` | bl 0x00bde270 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afaaac`](#insn-00afaaac) 範囲 `[['00afaaac', '00afaaaf']]`
  - `FALL_THROUGH` [`00afaaac`](#insn-00afaaac) → [`00afaab0`](#insn-00afaab0)
- ブロック [`00afaab0`](#insn-00afaab0) 範囲 `[['00afaab0', '00afaae3']]`
  - `CONDITIONAL_JUMP` [`00afaae0`](#insn-00afaae0) → [`00afab68`](#insn-00afab68)
  - `FALL_THROUGH` [`00afaae0`](#insn-00afaae0) → [`00afaae4`](#insn-00afaae4)
- ブロック [`00afaae4`](#insn-00afaae4) 範囲 `[['00afaae4', '00afaaff']]`
  - `CONDITIONAL_JUMP` [`00afaafc`](#insn-00afaafc) → [`00afab68`](#insn-00afab68)
  - `FALL_THROUGH` [`00afaafc`](#insn-00afaafc) → [`00afab00`](#insn-00afab00)
- ブロック [`00afab00`](#insn-00afab00) 範囲 `[['00afab00', '00afab0f']]`
  - `CONDITIONAL_JUMP` [`00afab0c`](#insn-00afab0c) → [`00afab20`](#insn-00afab20)
  - `FALL_THROUGH` [`00afab0c`](#insn-00afab0c) → [`00afab10`](#insn-00afab10)
- ブロック [`00afab10`](#insn-00afab10) 範囲 `[['00afab10', '00afab1b']]`
  - `CONDITIONAL_JUMP` [`00afab18`](#insn-00afab18) → [`00afab40`](#insn-00afab40)
  - `FALL_THROUGH` [`00afab18`](#insn-00afab18) → [`00afab1c`](#insn-00afab1c)
- ブロック [`00afab1c`](#insn-00afab1c) 範囲 `[['00afab1c', '00afab1f']]`
  - `UNCONDITIONAL_JUMP` [`00afab1c`](#insn-00afab1c) → [`00afab50`](#insn-00afab50)
- ブロック [`00afab20`](#insn-00afab20) 範囲 `[['00afab20', '00afab3f']]`
  - `FALL_THROUGH` [`00afab3c`](#insn-00afab3c) → [`00afab40`](#insn-00afab40)
- ブロック [`00afab40`](#insn-00afab40) 範囲 `[['00afab40', '00afab47']]`
  - `FALL_THROUGH` [`00afab44`](#insn-00afab44) → [`00afab48`](#insn-00afab48)
- ブロック [`00afab48`](#insn-00afab48) 範囲 `[['00afab48', '00afab4f']]`
  - `FALL_THROUGH` [`00afab4c`](#insn-00afab4c) → [`00afab50`](#insn-00afab50)
- ブロック [`00afab50`](#insn-00afab50) 範囲 `[['00afab50', '00afab67']]`
- ブロック [`00afab68`](#insn-00afab68) 範囲 `[['00afab68', '00afab6b']]`

## 命令位置別の参照

- [`00afaaac`](#insn-00afaaac) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaab0`](#insn-00afaab0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaab4`](#insn-00afaab4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaab8`](#insn-00afaab8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaae0`](#insn-00afaae0) → [`00afab68`](#insn-00afab68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaafc`](#insn-00afaafc) → [`00afab68`](#insn-00afab68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab0c`](#insn-00afab0c) → [`00afab20`](#insn-00afab20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab18`](#insn-00afab18) → [`00afab40`](#insn-00afab40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab1c`](#insn-00afab1c) → [`00afab50`](#insn-00afab50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab2c`](#insn-00afab2c) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00afab4c`](#insn-00afab4c) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00afab54`](#insn-00afab54) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab58`](#insn-00afab58) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab5c`](#insn-00afab5c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab68`](#insn-00afab68) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afaaac`](#insn-00afaaac)

~~~json
{
  "source": "00afaaac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaab0`](#insn-00afaab0)

~~~json
{
  "source": "00afaab0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaab4`](#insn-00afaab4)

~~~json
{
  "source": "00afaab4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaab8`](#insn-00afaab8)

~~~json
{
  "source": "00afaab8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaae0`](#insn-00afaae0)

~~~json
{
  "source": "00afaae0",
  "target": "00afab68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaafc`](#insn-00afaafc)

~~~json
{
  "source": "00afaafc",
  "target": "00afab68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab0c`](#insn-00afab0c)

~~~json
{
  "source": "00afab0c",
  "target": "00afab20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab18`](#insn-00afab18)

~~~json
{
  "source": "00afab18",
  "target": "00afab40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab1c`](#insn-00afab1c)

~~~json
{
  "source": "00afab1c",
  "target": "00afab50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab2c`](#insn-00afab2c)

~~~json
{
  "source": "00afab2c",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afab4c`](#insn-00afab4c)

~~~json
{
  "source": "00afab4c",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afab54`](#insn-00afab54)

~~~json
{
  "source": "00afab54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab58`](#insn-00afab58)

~~~json
{
  "source": "00afab58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab5c`](#insn-00afab5c)

~~~json
{
  "source": "00afab5c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab68`](#insn-00afab68)

~~~json
{
  "source": "00afab68",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
