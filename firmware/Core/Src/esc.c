/*
 * esc.c
 *
 *  Created on: Nov 22, 2026
 *      Author: dhruvilshukla
 */

#include "esc.h"
#include "main.h"
#include "tim.h"

#define ESC_MIN_US 1000
#define ESC_MAX_US 1200

void esc_set_us(uint16_t us)
{
	if (us < ESC_MIN_US) us = ESC_MIN_US;
	if (us > ESC_MAX_US) us = ESC_MAX_US;

	__HAL_TIM_SET_COMPARE(&htim3, TIM_CHANNEL_3, us);

}

void esc_init(void)
{
	HAL_TIM_PWM_Start(&htim3, TIM_CHANNEL_3);
	esc_set_us(ESC_MIN_US);
}


